//loading......
var myGlobalHandlers = {
	onCreate: function(){
		$('systemWorking').style.display="none";
		Element.show('systemWorking');
	},
	onComplete: function() {
		if(Ajax.activeRequestCount == 0){
			Element.hide('systemWorking');
		}
	}
};
Ajax.Responders.register(myGlobalHandlers);

//clean str space.
function trim(str){
  var regExp=/^\s*(.*?)\s*$/;
  return str.replace(regExp, "$1");
}

//post HostForm form.
function HostForm_SubmitCheck(obj)
{
    url_string=trim($F('HostDomain'));
    appname=trim($F('AppName'));

    if (appname=="")
        {
            ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：请输入需监控应用名称！'});
            document.HostForm.appname.focus();
            return false;
        }

    if (url_string=="")
        {
            ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：请输入需监控的URL！'});
            document.HostForm.HostDomain.focus();
            return false;
        }

    if ($("status").checked==false && $("responsechar").value=="")
        {
            ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：请选择一种探测规则！'});
            return false;
        }

    obj.submit();
}

//check response status
function Status_check()
{
    if ($("status").checked==true)
    {
        $("responsechar").disabled=true;
        $("responsechar").value="";
    }
    else
        $("responsechar").disabled=false;
}

function CheckSearchForm()
{
	if (trim($F('StartTime'))!="")
	{
		if (trim($F('EndTime'))=="")
		{
			ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'请输入结束时间！'});
			return;
		}
		
		if (document.SearchForm.StartTime.value > document.SearchForm.EndTime.value)
		{
			ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'开始时间大于结束时间?'});
			return;
		}
	}

	if (trim($F('EndTime'))!="")
	{
		if (trim($F('StartTime'))=="")
		{
			ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'请输入开始时间！'});
			return;
		}
	}
	document.SearchForm.action="/webmonitor/";
	document.SearchForm.submit();
}

function CheckReportForm()
{
	if ($F('Reporttype')=="userdefind")
	{
		if (trim($F('StartTime'))=="" || trim($F('EndTime'))=="")
		{
			ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'自定义报表需要输入开始或结束时间！'});
			return;
		}
	}
	document.SearchForm.action="/webmonitor/report";
	document.SearchForm.submit();
}

function Reloaddate()
{
	$('StartTime').value='';
	$('EndTime').value='';
}