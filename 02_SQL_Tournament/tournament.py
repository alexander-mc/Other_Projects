#!/usr/bin/env python

# Implementation of a Swiss-system tournament
# -----------------------------------

import psycopg2

def connect():
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    conn = connect()
    c = conn.cursor()
    query = "DELETE from matches;"
    c.execute(query)
    conn.commit()
    conn.close()

def deletePlayers():
    conn = connect()
    c = conn.cursor()
    query = "DELETE from players;"
    c.execute(query)
    conn.commit()
    conn.close()

def countPlayers():
    conn = connect()
    c = conn.cursor()
    query = "SELECT count (*) from players;"
    c.execute(query)
    results = c.fetchall()[0][0]
    return results
    conn.commit()
    conn.close()

def registerPlayer(name):
    conn = connect()
    c = conn.cursor()
    """The below line of code uses DEFAULT, however the code will run just fine without 'player_ID' and 'DEFAULT' columns. See the function 'reportMatch' on how this is done."""
    c.execute("INSERT INTO players (player_id, player_name) VALUES (DEFAULT,%s)", (name,))
    conn.commit()
    conn.close()

def playerStandings():
    conn = connect()
    c = conn.cursor()
    c.execute("""
       SELECT players.player_ID,
       players.player_name,
       subq1.won,
       subq2.matches

       from players

       left join
            (select players.player_ID, count(won) as won
                from matches
                right join players
                on players.player_ID = matches.won
                group by player_ID
                ) as subq1
            on players.player_ID = subq1.player_ID

        left join
            (select players.player_ID, count (won_and_lost) as matches
                from (
                    select won as won_and_lost
                    from matches
                    union all
                    select lost from matches)
                    as won_and_lost_subq
                right join players
                on won_and_lost_subq.won_and_lost = players.player_ID
                group by Player_ID
            ) as subq2
            on players.player_ID = subq2.player_ID

        order by won desc
        ;""")
    results = c.fetchall()
    return results
    conn.commit()
    conn.close()

def reportMatch(winner, loser):
    conn = connect()
    c = conn.cursor()
    """In the below code, no DEFAULT column is designated, unlike the code written in the function 'registerPlayer'"""
    c.execute("INSERT INTO matches (won, lost) VALUES (%s,%s)", (winner,loser,))
    conn.commit()
    conn.close()
 
def swissPairings():

    standings = playerStandings()
    pairings = []

    for i in range(0,len(standings)-1,2):
        id1 = standings[i][0]
        name1 = standings[i][1]
        id2 = standings[i+1][0]
        name2 = standings[i+1][1]
        pairings.append((id1, name1, id2, name2))

    return pairings
    