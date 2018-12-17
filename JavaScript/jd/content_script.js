window.onload = function(){
	document.getElementById("viewOrderMobile").click(); //商家后台客户电话号码默认隐藏，需要点击显示
	if(document.querySelectorAll('td.ordinf-td')[3].querySelectorAll('td')[3]&&document.querySelectorAll('td.ordinf-td')[3].querySelectorAll('td')[3].innerHTML != "个人"){
		document.body.style.backgroundColor = "red" //当客户对发票抬头有要求时页面背景变为红色，更为醒目
	};
	//var a = document.getElementById('receiveData').innerHTML; 待继续开发
	//var additionalInfo = {
		//"selection": a
	//};
	//chrome.runtime.connect().postMessage(additionalInfo);
}
