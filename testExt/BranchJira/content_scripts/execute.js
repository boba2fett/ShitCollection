(function() {
  if (window.hasRun) {
    return;
  }
  window.hasRun = true;


  const umlautMap = {
    '\u00dc': 'UE',
    '\u00c4': 'AE',
    '\u00d6': 'OE',
    '\u00fc': 'ue',
    '\u00e4': 'ae',
    '\u00f6': 'oe',
    '\u00df': 'ss',
  }
  
  function replaceUmlaute(str) {
    return str
      .replace(/[\u00dc|\u00c4|\u00d6][a-z]/g, (a) => {
        const big = umlautMap[a.slice(0, 1)];
        return big.charAt(0) + big.charAt(1).toLowerCase() + a.slice(1);
      })
      .replace(new RegExp('['+Object.keys(umlautMap).join('|')+']',"g"),
        (a) => umlautMap[a]
      );
  }

  function doAction(action) {
    if(action==="Branch")
    {
      var typSp = document.querySelector('span[id^="type-val"]');
      var a = document.querySelector('a[id^="key-val"]');
      var h = document.querySelector('h1[id^="summary-val"]');

      var issue=a.textContent;
      var desc=h.textContent;

      desc=replaceUmlaute(desc);
      desc=desc.replace(" ","_");
      desc=desc.replace(/[^a-zA-Z0-9]/g,'_');

      if(typSp.textContent.includes("Bug"))
      {
          var branch="bugfix/"+issue+"_"+desc;
          navigator.clipboard.writeText(branch);
      }
      else{
        if(typSp.textContent.includes("User Story"))
        {
            var branch="feature/"+issue+"_"+desc+"/develop";
            navigator.clipboard.writeText(branch);
        }
        else{
          if(typSp.textContent.includes("Technical Task"))
          {
              var aPar = document.querySelector('a[id^="parent_issue_summary"]');
              var parentDesc=aPar.textContent;
              parentDesc=replaceUmlaute(parentDesc);
              parentDesc=parentDesc.replace(" ","_");
              parentDesc=parentDesc.replace(/[^a-zA-Z0-9\-]/g,'_');
              parent="feature/"+parentDesc+"/";
              var branch=parent+issue+"_"+desc+"";
              console.log(branch)
              navigator.clipboard.writeText(branch);
          }
        }
      }
    }
    if(action==="Commit-Message")
    {
      var typSp = document.querySelector('span[id^="type-val"]');
      var a = document.querySelector('a[id^="key-val"]');
      var h = document.querySelector('h1[id^="summary-val"]');

      var issue=a.textContent;
      var desc=h.textContent;

      msg=issue+desc+":\n";
      navigator.clipboard.writeText(msg);
    }
  }

  browser.runtime.onMessage.addListener((message) => {
    if (message.command === "cmd") {
      doAction(message.action);
    }
  });

})();
