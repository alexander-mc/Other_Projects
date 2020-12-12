/* -+-+-+-+- "MODEL" -+-+-+-+- */

var htmlPuppyName = document.getElementById('puppy-name');
var htmlPuppyMsg = document.getElementById('puppy-msg');
var htmlPuppyImage = document.getElementById('puppy-image');
var htmlPuppyList = document.getElementById('puppy-list');
var htmlAdminForm = document.getElementById('admin-form-container');
var htmlShowAdminButton = document.getElementById('show-admin-button');
var htmlAdminButton = document.getElementById('admin-button');
var htmlShowPuppyInfo = document.getElementById('show-puppy-info');
var htmlFormName = document.getElementById('form-name');
var htmlFormImgURL = document.getElementById('form-img-url');
var htmlFormNumClicks = document.getElementById('form-num-clicks');
var htmlSaveButton = document.getElementById('savebtn');
var htmlCancelButton = document.getElementById('cancelbtn');
var htmlListElem, currentPuppyId, onlineImgUrl, testUrlImg;

var allPuppies = [{
		name : 'Buddy',
		clickMsg: 'Woof! x',
		clickCount : 0,
		imgUrlRel : 'images/puppy1.jpg',
		imgUrlAbs : 'http://www.lifewithdogs.tv/wp-content/uploads/2014/03/3.21.14-National-Puppy-Day5.jpg'
	},
	{
		name : 'Happy',
		clickMsg: 'Woof! x',
		clickCount : 0,
		imgUrlRel : 'images/puppy2.jpg',
		imgUrlAbs : 'http://cdn.attackofthecute.com/August-05-2012-02-06-05-tqqqq.jpg'
	},
	{
		name : 'Scout',
		clickMsg: 'Woof! x',
		clickCount : 0,
		imgUrlRel : 'images/puppy3.jpg',
		imgUrlAbs : 'https://i.pinimg.com/originals/d6/0f/36/d60f361fd091bc4002d2f47b522cc649.jpg'
	},
	{
		name : 'Batman',
		clickMsg: 'Woof! x',
		clickCount : 0,
		imgUrlRel : 'images/puppy4.jpg',
		imgUrlAbs : 'http://images6.fanpop.com/image/photos/35200000/Puppy-dogs-35247732-500-313.jpg'
	},
	{
		name : 'Chance',
		clickMsg: 'Woof! x',
		clickCount : 0,
		imgUrlRel : 'images/puppy5.jpg',
		imgUrlAbs : 'https://www.guidedogswa.com.au/wp-content/uploads/2016/01/20160420_PuppyRaising_3.jpg'
	}]

/* -+-+-+-+- "OCTOPUS" -+-+-+-+- */

var octopus = {

	init: function() {
		currentPuppyId = 0;

		view.setDisplay(htmlShowPuppyInfo, false);
		view.setDisplay(htmlAdminForm, false);

		onlineImgUrl = false;

		view.createPuppyList();
		view.updatePuppyInfo(currentPuppyId);

		octopus.clickListElem();
		octopus.clickImg();
		octopus.clickAdmin();
		octopus.clickSave();
		octopus.clickCancel();
	},

	clickListElem: function(){
		htmlPuppyList.addEventListener('click', function(e) {
			if(e.target && e.target.nodeName == 'LI') {
				var str = e.target.id;
				currentPuppyId = str.split('-').pop();
				view.updatePuppyInfo(currentPuppyId);
				view.setDisplay(htmlShowPuppyInfo, true);
				view.setDisplay(htmlAdminForm, false);
				view.setDisplay(htmlShowAdminButton, true);
			}
		});
	},

	clickImg: function(){
		htmlPuppyImage.addEventListener('click', function(){
			allPuppies[currentPuppyId].clickCount += 1;
			view.updateListElem(currentPuppyId);
			view.updatePuppyInfo(currentPuppyId);
			view.setDisplay(htmlAdminForm, false);
			view.setDisplay(htmlShowAdminButton, true);
		}, false);
	},

	clickAdmin: function() {
		htmlAdminButton.addEventListener('click', function(){
			view.setDisplay(htmlShowAdminButton, false);
			view.setDisplay(htmlAdminForm, true);
			view.updateAdminForm();
		}, false);
	},

	clickSave: function() {
		var numErrors = false;
		htmlSaveButton.addEventListener('click', function(){
			
			try {
				if (htmlFormNumClicks.value == "" || isNaN(htmlFormNumClicks.value) || htmlFormNumClicks.value % 1 !== 0 || htmlFormNumClicks.value < 0) throw "Please enter a positive whole value for the number of clicks!";
				if (htmlFormName.value == "") throw "Please give your puppy a name!";
				if (htmlFormImgURL.value == "") throw "Please include the image URL of your puppy!";
			}

			catch(err) {				
				numErrors = true;
				alert("Error: " + err);
			}

			if (numErrors == true) {
				numErrors = false;
				return;
			}
			else {
				octopus.testUrl();
				testUrlImg.onerror(0);
			}
		}, false);
	},

	testUrl: function() {
		var oldPuppyName = octopus.getPuppyName(currentPuppyId);
		var oldPuppyImgSrc = octopus.getPuppyImgSrc(currentPuppyId);
		var oldPuppyCount = octopus.getPuppyCount(currentPuppyId);

		testUrlImg = new Image();
		testUrlImg.src = htmlFormImgURL.value;	
		testUrlImg.onerror = function(x) {

			if (x == 0) {
				return octopus.getFormInfo();
			}

			else {
				invalidImg = function () {
					alert('Error: Unable to load your puppy image. Please use a different image URL.');
					allPuppies[currentPuppyId].name = oldPuppyName
					allPuppies[currentPuppyId].clickCount = oldPuppyCount
					if (onlineImgUrl == false) {
						allPuppies[currentPuppyId].imgUrlRel = oldPuppyImgSrc;		
					}
					else {
						allPuppies[currentPuppyId].imgUrlAbs = oldPuppyImgSrc;
					}
					view.updatePuppyInfo(currentPuppyId);
					view.updateListElem(currentPuppyId);
					view.setDisplay(htmlAdminForm, true);
					view.setDisplay(htmlShowAdminButton, false);
				}
				invalidImg();		
			}
		}
	},

	clickCancel: function() {
		htmlCancelButton.addEventListener('click', function(){
			view.setDisplay(htmlAdminForm, false);
			view.setDisplay(htmlShowAdminButton, true);
		}, false);
	},

	getPuppyName: function(puppyId) {
		return allPuppies[puppyId].name;
	},

	getPuppyCount: function(puppyId) {
		return allPuppies[puppyId].clickCount;
	},
	
	getPuppyMsg: function(puppyId) {
		return allPuppies[puppyId].clickMsg + allPuppies[puppyId].clickCount;
	},

	getPuppyImgSrc: function(puppyId) {
		if (onlineImgUrl == false) {
			return allPuppies[puppyId].imgUrlRel;			
		}
		else {
			return allPuppies[puppyId].imgUrlAbs;
		}
	},

	storePuppyImgSrc: function(puppyId) {
		if (onlineImgUrl == false) {
			allPuppies[puppyId].imgUrlRel = htmlFormImgURL.value;		
		}
		else {
			allPuppies[puppyId].imgUrlAbs = htmlFormImgURL.value;
		}
	},

	getFormInfo: function() {
		allPuppies[currentPuppyId].name = htmlFormName.value;
		allPuppies[currentPuppyId].clickCount = parseInt(htmlFormNumClicks.value);
		octopus.storePuppyImgSrc(currentPuppyId);

		view.updateListElem(currentPuppyId);	
		view.updatePuppyInfo(currentPuppyId);
		view.setDisplay(htmlAdminForm, false);
		view.setDisplay(htmlShowAdminButton, true);
	}
};

/* -+-+-+-+- "VIEW" -+-+-+-+- */

var view = {

	createPuppyList: function() {
		for (var i = 0; i < allPuppies.length; i++) {
			htmlListElem = document.createElement('li');
			htmlListElem.setAttribute('id', 'puppy-list-' + i);
			htmlListElem.setAttribute('class', 'puppy-list-elements');
			htmlPuppyList.insertBefore(htmlListElem, htmlPuppyList.lastChild);
			view.updateListElem(i);
		}
	},

	updateListElem: function(puppyId) {
		htmlListElem = document.getElementById('puppy-list-' + puppyId);
		return htmlListElem.textContent = octopus.getPuppyName(puppyId) + ' (' + octopus.getPuppyCount(puppyId) + ')';
	},

	updatePuppyInfo: function(puppyId) {
		htmlPuppyName.textContent = octopus.getPuppyName(puppyId);
		htmlPuppyImage.src = octopus.getPuppyImgSrc(puppyId);
		htmlPuppyMsg.textContent = octopus.getPuppyMsg(puppyId);
	},

	setDisplay: function(element, value) {
		if (value == true) {
			element.style.display ='block';
		}
		else {
			element.style.display = 'none';
		}
	},

	updateAdminForm: function() {
		htmlFormName.value = octopus.getPuppyName(currentPuppyId);
		htmlFormImgURL.value = octopus.getPuppyImgSrc(currentPuppyId);
		htmlFormNumClicks.value = octopus.getPuppyCount(currentPuppyId);
	}
};

/* -+-+-+-+- Run the program! -+-+-+-+- */

octopus.init();
