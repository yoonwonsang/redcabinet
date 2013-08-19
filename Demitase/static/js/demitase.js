//var baseUrl = 'http://www.demitase.com/';
var baseUrl = 'http://127.0.0.1:8000/';
var stream = [];
var hotkeys = [];
var cntlist = [];
var keycnt = 0;
var tmp = 0;
var apicnt = 100;
var keySelection;

var doLogout = function() {
	alert("Real.....ly???");
	location.replace(baseUrl + 'logout/');
}

var doGetTimeline = function() {
	$.ajax({
		url : baseUrl + 'demitase_init/',
		async : false,
		success : function(data) {
			for (var num = 0; num < data.api_cnt; num++){
				// alert("MoreTimeline Get :" + num);
			    doGetMoreTimeline(num, data.my_id);	

			}
		},
		error : function() {
			alert("Fail to Load API");
		},
	});

}


var doGetMoreTimeline = function(num, my_id) {
	$.ajax({ 
		type : 'get',
		url : baseUrl + 'demitase/',
		data : {query:num, id:my_id},
		async : false,
		success : function(data) {
			for (var i in data) {
				stream.push(data[i]);
				doAppend(data[i]);
			}
			doSortHotkeys();
			doShowKeys(hotkeys);
			
		},
		error : function() {
			alert("Fail to get data!");
		},
	});
}


var doSortHotkeys = function(){
	cntlist = [];
	for (var i = 0; i < hotkeys.length; i++){
		for (var j = 0; j < hotkeys.length; j++){
			if(hotkeys[i].count >= hotkeys[j].count && i != j){
				tmp_key = hotkeys[i].keyword;
				tmp_cnt = hotkeys[i].count;
				hotkeys[i].keyword = hotkeys[j].keyword;
				hotkeys[i].count = hotkeys[j].count;
				hotkeys[j].keyword = tmp_key;
				hotkeys[j].count = tmp_cnt;
				continue;
			} else {
				continue;
			}
		}
	}
	for (var i = 0; i < hotkeys.length; i++){
		if ( tmp == hotkeys[i].count ){
			continue;
		} else {
			cntlist.push(hotkeys[i].count);
			tmp = hotkeys[i].count;
		}
	}
}


var doAppend = function(data) {
	// alert($('#selectedKey').html());
	if (keySelection) {
		for (var i in data.keywords) {
			if (keySelection == data.keywords[i]){
				node = $('#msgTemplate').clone();
				$('.name', node).append(data.username);
				$('.content', node).append(data.text);
				$('.date', node).append(data.date);
				node.show();
				$('#timelinearea').append(node);
			}
		}
	} else {
	// alert("test");
		node = $('#msgTemplate').clone();
		$('.name', node).append(data.username);
		$('.content', node).append(data.text);
		$('.date', node).append(data.date);
		node.show();	
		$('#timelinearea').append(node);
	}
	for (var i in data.keywords){
		$('.key'+i, node).append(data.keywords[i]);
		doSumKeywords(data.keywords[i]);
	}
}

var doAppend2 = function(data) {
	// alert($('#selectedKey').html());
	if (keySelection) {
		for (var i in data.keywords) {
			if (keySelection == data.keywords[i]){
				node = $('#msgTemplate').clone();
				$('.name', node).append(data.username);
				$('.content', node).append(data.text);
				$('.date', node).append(data.date);
				node.show();
				$('#timelinearea').append(node);
			}
		}
	} else {
	// alert("test");
		node = $('#msgTemplate').clone();
		$('.name', node).append(data.username);
		$('.content', node).append(data.text);
		$('.date', node).append(data.date);
		node.show();	
		$('#timelinearea').append(node);
	}
}

var doShowKeys = function() {
	$('#keylistarea').empty();
	for (var i = 0; i < hotkeys.length; i++ ){
			// alert("KeyCnt: "+keycnt+"\nResult: "+hotkeys[keycnt].count);
		if(hotkeys[i].count == cntlist[0]){
			badge_style = "badge badge-important";
		} else if(hotkeys[i].count == cntlist[1]){
			badge_style = "badge badge-warning";
		} else if(hotkeys[i].count == cntlist[2]){
			badge_style = "badge badge-success";
		} else if(hotkeys[i].count == cntlist[3]){
			badge_style = "badge badge-info";
		} else {
			badge_style = "badge";
		}
		node = $('#sortedKeys').clone();
		$('.word', node).append(hotkeys[i].keyword);
		node.append("<span class=\"count_badge "+badge_style+"\">"+hotkeys[i].count+"</span>")
		// $('.count_badge', node).append(hotkeys[keycnt].count);
		node.show();
		$('#keylistarea').append(node);
	}
	$('#lessMoreKeys').show();
	$('#keylistarea').append($('#lessMoreKeys'));
}


var doSeeMoreKeys = function() {
	doShowKeys();
}

var doReloadKeys = function() {
	$('#lessMoreKeys').remove();
	$('#keylistarea').empty();
	keycnt = 0;
	doShowKeys();
}

var doSumKeywords = function(word){
	if (hotkeys.length == 0){
		hotkeys.push({keyword:word,count:1});
		// alert("type: 1, word: "+word);
	} else {
		for (var i in hotkeys){
			// alert("array["+i+"] key: "+hotkeys[i].keyword+" word: "+word);
			if (hotkeys[i].keyword == word){
				hotkeys[i].count += 1;
				// alert("type: 2, word: "+word);
				break;
			}
			else {
				if( i == hotkeys.length-1){
					// alert("type: 4, word: "+word);
					hotkeys.push({keyword:word,count:1});
				} else {
					// alert("type: 3, word: "+word);
					continue;
				}
			}

		}
	}
}

var doSelectKeyword = function() {

	keySelection = $('.word', $(this)).html();

	$('#selectedKey').html(keySelection);
	doClear();
	for (var i in stream){
		for (var j in stream[i].keywords){
			if(stream[i].keywords[j] == keySelection){
				doAppend2(stream[i]);
			} else {
				continue;
			}
		}
	}
}

var doShowAllTimeline = function() {
	doClear();
	keySelection = '';
	$('#selectedKey').html("Select a Keyword");
	for (var i in stream){
		doAppend(stream[i]);
	}
}

var doReload = function() {
	doClear();
	doGetTimeline();
}

var doClear = function() {
	$('#timelinearea').html('')
}


// // UTILITY METHODS
// function setCookie(name, value, day) {
// 	var expire = new Date();
// 	expire.setDate(expire.getDate() + day);
// 	cookies = name + '=' + escape(value) + '; path=/ ';
// 	if (typeof day != 'undefined')
// 		cookies += ';expires=' + expire.toGMTString() + ';';
// 	document.cookie = cookies;
// }
// 
// function getCookie(name) {
// 	name = name + '=';
// 	var cookieData = document.cookie;
// 	var start = cookieData.indexOf(name);
// 
// 	var value = '';
// 	if (start != -1) {
// 		start += name.length;
// 		var end = cookieData.indexOf(';', start);
// 		if (end == -1)
// 			end = cookieData.length;
// 		value = cookieData.substring(start, end);
// 	}
// 	return unescape(value);
// }

