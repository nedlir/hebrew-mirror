////////////
// CLOCK //
//////////
var currentSec = getSecondsToday();

var seconds = (currentSec / 60) % 1;
var minutes = (currentSec / 3600) % 1;
var hours = (currentSec / 43200) % 1;

setTime(60 * seconds, "second");
setTime(3600 * minutes, "minute");
setTime(43200 * hours, "hour");

function setTime(left, hand) {
	$(".clock__" + hand).css("animation-delay", "" + left * -1 + "s");
}

function getSecondsToday() {
	let now = new Date();

	let today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

	let diff = now - today;
	return Math.round(diff / 1000);
}


//////////////////
// FULL SCREEN //
////////////////
function go_full_screen() {
	var elem = document.documentElement;
	if (elem.requestFullscreen) {
		elem.requestFullscreen();
	} else if (elem.msRequestFullscreen) {
		elem.msRequestFullscreen();
	} else if (elem.mozRequestFullScreen) {
		elem.mozRequestFullScreen();
	} else if (elem.webkitRequestFullscreen) {
		elem.webkitRequestFullscreen();
	}
}


//////////////////
// NEWS TICKER //
////////////////


var tickerIndex = 0;
var tickerDuration = 4;
var ticker;

var setTicker = function () {
	ticker.text(tickerItems[tickerIndex++]);
	if (tickerIndex >= tickerItems.length) {
		tickerIndex = 0;
	}
};

var rotateTicker = function () {
	ticker.fadeOut('slow', function () {
		setTicker();
		ticker.fadeIn('slow');
	});
};

$(document).ready(function () {
	ticker = $('span#ticker');
	setTicker();
	if (tickerItems.length > 1) {
		window.setInterval(rotateTicker, tickerDuration * 1000);
	}
});