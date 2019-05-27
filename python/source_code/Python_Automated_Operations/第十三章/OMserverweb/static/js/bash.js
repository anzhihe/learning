//--------把中文字符转换成Utf8编码------------------------//
 function EncodeUtf8(s1)
  {
      var s = escape(s1);
      var sa = s.split("%");
      var retV ="";
      if(sa[0] != "")
      {
         retV = sa[0];
      }
      for(var i = 1; i < sa.length; i ++)
      {
           if(sa[i].substring(0,1) == "u")
           {
               retV += Hex2Utf8(Str2Hex(sa[i].substring(1,5)));
              
           }
           else retV += "%" + sa[i];
      }
     
      return retV;
  }
  function Str2Hex(s)
  {
      var c = "";
      var n;
      var ss = "0123456789ABCDEF";
      var digS = "";
      for(var i = 0; i < s.length; i ++)
      {
         c = s.charAt(i);
         n = ss.indexOf(c);
         digS += Dec2Dig(eval(n));
          
      }
      //return value;
      return digS;
  }
  function Dec2Dig(n1)
  {
      var s = "";
      var n2 = 0;
      for(var i = 0; i < 4; i++)
      {
         n2 = Math.pow(2,3 - i);
         if(n1 >= n2)
         {
            s += 1;
            n1 = n1 - n2;
          }
         else
          s += 0;
         
      }
      return s;
     
  }
  function Dig2Dec(s)
  {
      var retV = 0;
      if(s.length == 4)
      {
          for(var i = 0; i < 4; i ++)
          {
              retV += eval(s.charAt(i)) * Math.pow(2, 3 - i);
          }
          return retV;
      }
      return -1;
  }
  function Hex2Utf8(s)
  {
     var retS = "";
     var tempS = "";
     var ss = "";
     if(s.length == 16)
     {
         tempS = "1110" + s.substring(0, 4);
         tempS += "10" +  s.substring(4, 10);
         tempS += "10" + s.substring(10,16);
         var sss = "0123456789ABCDEF";
         for(var i = 0; i < 3; i ++)
         {
            retS += "%";
            ss = tempS.substring(i * 8, (eval(i)+1)*8);
           
           
           
            retS += sss.charAt(Dig2Dec(ss.substring(0,4)));
            retS += sss.charAt(Dig2Dec(ss.substring(4,8)));
         }
         return retS;
     }
     return "";
  } 

//HTML转义方法
function html_decode(str)  
{  
  var s = "";  
  if (str.length == 0) return "";  
  s = str.replace(/&gt;/g, "&");  
  s = s.replace(/&lt;/g, "<");  
  s = s.replace(/&gt;/g, ">");  
  s = s.replace(/&nbsp;/g, " ");  
  s = s.replace(/&#39;/g, "\'");  
  s = s.replace(/&quot;/g, "\"");  
  s = s.replace(/<br>/g, "\n");  
  return s;  
}

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


//加载一级菜单;
function submitleavel()
{
	var url = '/autoadmin/server_fun_categ/';
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{
        document.getElementById("serverclass").options.length=0;
		eval("var resultString='"+originalRequest.responseText+"'"); 
		var objarray=resultString.split("|"); 
        var soojs_value=objarray[1].split(","); 
        var soojs_text=objarray[0].split(","); 
	    for ( var i=0;i<soojs_value.length;i++){
	    	var oOption= document.createElement("OPTION");  
    	 	oOption.value=soojs_value[i];  
     		oOption.text=soojs_text[i];  
     		document.systemForm.serverclass.options.add(oOption);
		}
	}
}


//加载二级菜单;
function submitleave2(currvalue)
{
   	if (currvalue==-1)
		return false;
	document.getElementById("serverAppclass").options.length=0;
	var oOption_load= document.createElement("OPTION");  
 	oOption_load.value=[-1];  
	oOption_load.text='正在加载...';  
	document.systemForm.serverAppclass.options.add(oOption_load);	
	var url = '/autoadmin/server_app_categ/?fun_categId='+currvalue;
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{		
		document.getElementById("serverAppclass").options.length=0;
		eval("var resultString='"+originalRequest.responseText+"'"); 
		var objarray=resultString.split("|"); 
        var soojs_value=objarray[1].split(","); 
        var soojs_text=objarray[0].split(","); 
	    for ( var i=0;i<soojs_value.length;i++){
	    	var oOption= document.createElement("OPTION");  
    	 	oOption.value=soojs_value[i];  
     		oOption.text=soojs_text[i];  
     		document.systemForm.serverAppclass.options.add(oOption);
		}
	}
}


//加载三级菜单;
function submitleave3(currvalue)
{
   	if (currvalue==-1)
		return false;
	document.getElementById("serverApplist").options.length=0;
	var oOption_load= document.createElement("OPTION");  
 	oOption_load.value=[-1];  
	oOption_load.text='正在加载...';  
	document.systemForm.serverApplist.options.add(oOption_load);	
	var url = '/autoadmin/server_list/?app_categId='+currvalue;
	//url=EncodeUtf8(url);
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{		
		document.getElementById("serverApplist").options.length=0;
		eval("var resultString='"+originalRequest.responseText+"'"); 
		var objarray=resultString.split("|"); 
        var soojs_value=objarray[1].split(","); 
        var soojs_text=objarray[0].split(","); 
	    for ( var i=0;i<soojs_value.length;i++){
	    	var oOption= document.createElement("OPTION");  
    	 	oOption.value=soojs_value[i];  
     		oOption.text=soojs_text[i];  
     		document.systemForm.serverApplist.options.add(oOption);
		}
	}
}

function checkform(checkid)
{
	if (document.getElementById("sys_param_1"))
    	b=$F('sys_param_1');
	
	if (document.getElementById("sys_param_2"))
    	c=$F('sys_param_2');

    switch (checkid)
    {
        case 1:
            if (b=="")
            {
                ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：模块扩展（1）表单域不能为空！'})
                return false;
            }
            break;
 
        case 2:
            if (c=="")
            {
                ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：模块扩展（2）表单域不能为空！'})
                return false;
            }
            break;

        case 3:
            if ((b=="") && (c==""))
            {
                ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：模块扩展（1）或模块扩展（2）表单域不能为空！'})
                return false;
            }
            break;
        
        default:
            return true;
    }
    return true;
}

//提交模块;
function submitmodule()
{
	//$('placeholder').innerHTML ="";
	urlpar=""
	if ($F('modules')==-1)
	{
        ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：请选择需要操作的模块！'})
        return false;
	}

	if ($F('serverApplist')==null || $F('serverApplist')=="")
	{
        ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：请选择服务器IP！'})
        return false;
	}
	else
	    serverappvalue=$F('serverApplist');

	if (document.getElementById("sys_param_1"))
	{
		if (!checkform(1))
			return false;
		urlpar+="&sys_param_1="+$F('sys_param_1')
	}
	if (document.getElementById("sys_param_2"))
	{
		if (!checkform(2))
			return false;
		urlpar+="&sys_param_2="+$F('sys_param_2')
	}
	var serverlist="";
	for(var i=0; i<=serverappvalue.length-1; i++)
	{
		serverlist+=serverappvalue[i].replace('*',' ')+'\n';
	}
	if (!confirm("- - - - - - -提交确认- - - - - - -\n\n命令名称："+$F("ModuleName")+"\n\n操作对象：\n"+serverlist))
		return false;

	var url = '/autoadmin/module_run/?ModuleID='+$F("ModuleID")+'&hosts='+serverappvalue+urlpar;
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{		
		$('placeholder').innerHTML = originalRequest.responseText+'<br>'+$('placeholder').innerHTML;
	}
}

//提交安全监视;
function submitaudit()
{
	//$('placeholder').innerHTML ="";
	urlpar=""
	if ($F('serverApplist')!=null && $F('serverApplist')!="")
	{
		serverappvalue=$F('serverApplist');
	}
	else
		serverappvalue=""
	    
	var url = '/omaudit/omaudit_run/?LastID='+$F("LastID")+'&hosts='+serverappvalue;
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{		
		eval("var resultString='"+originalRequest.responseText+"'"); 
		var	soojs_history_string="";
		var objarray=resultString.split("@@"); 

        var soojs_historys=objarray[0].split("*");
		if (soojs_historys.length==1)
		{
			return false;	
			}

        var soojs_lastid=objarray[1]; 
		document.getElementById("LastID").value = soojs_lastid
		for ( var i=0;i<soojs_historys.length;i++){
			soojs_history_string  = soojs_history_string + soojs_historys[i]+'<br>';  
		}
		$('placeholder').innerHTML = soojs_history_string.substring(0,soojs_history_string.length-4) +$('placeholder').innerHTML;
	}
}

function setIntervalAudit()
{
	timeId = setInterval("submitaudit();",3000);
	if ($F('sys_run_button')=="停止监视")
	{
		clearTimeout(timeId);
		document.getElementById("sys_run_button").value ="开始监视";
	}
	else
	{
		document.getElementById("sys_run_button").value ="停止监视";
	}
}

//提交添加模块;
function submitmodule_add()
{
	if ($F('module_name')==null || $F('module_name')=="")
	{
		ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：模块名称不能为空！'})
		return false;
	}

	if ($F('module_caption')==null || $F('module_caption')=="")
	{
		ymPrompt.alert({title:'系统提示：',width:350,height:150,message:'提交失败：模块描述不能为空！'})
		return false;
	}
	module_name=$F('module_name')
	module_caption=$F('module_caption')
	module_extend=$F('module_extend')
	
	var url = '/autoadmin/module_add_post/?module_name='+module_name+'&module_caption='+module_caption+'&module_extend='+module_extend;
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{		
		ymPrompt.alert({title:'系统提示：',width:350,height:150,message:originalRequest.responseText});
	}
}


function displayDIV(el) {
	whichEl = document.getElementById(el)
	whichEl.style.display   = 'block';
}

function hiddenDIV(el) {
	whichEl = document.getElementById(el)
	whichEl.style.display   = 'none';
}


//加载操作模块菜单;
function loadmodule()
{
	var url = '/autoadmin/module_list/';
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{
        document.getElementById("modules").options.length=0;
		eval("var resultString='"+originalRequest.responseText+"'"); 
		var objarray=resultString.split("|"); 
        var soojs_value=objarray[1].split(","); 
        var soojs_text=objarray[0].split(","); 
	    for ( var i=0;i<soojs_value.length;i++){
	    	var oOption= document.createElement("OPTION");  
    	 	oOption.value=soojs_value[i];  
     		oOption.text=soojs_text[i];  
     		document.getElementById("modules").options.add(oOption);
		}
	}
}

//加载模块信息;
function loadmoduleinfo(currvalue)
{
   	if (currvalue==-1)
		return false;
	var url = '/autoadmin/module_info/?Module_Id='+currvalue;
	var myAjax = new Ajax.Request(
	url,
	{
		method: 'get',
		onComplete: showResponse
	});
	function showResponse(originalRequest)
	{		
		eval("var resultString='"+originalRequest.responseText+"'"); 

		var objarray=resultString.split("@@"); 
        var module_id=objarray[0];  //module id
        var module_name=objarray[1];  //module name
        var module_caption=objarray[2];  //module caption
        var module_extend=objarray[3];  //module extend
		document.getElementById("ModuleID").value = module_id
		document.getElementById("ModuleName").value = module_name
		document.getElementById("module_name").innerText = "("+module_id+")"+module_name
		document.getElementById("module_caption").innerHTML = module_caption
		document.getElementById("module_extend").innerHTML = module_extend
	}
	

}