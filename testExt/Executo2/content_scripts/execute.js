(function() {
  if (window.hasRun) {
    return;
  }
  window.hasRun = true;

  function doAction(action) {
    console.log(action);
    if(action==="show_pwd")
    {
      var inputs = document.querySelectorAll('input[type^="password"]');
      for (i = 0; i < inputs.length; i++) {
          inputs[i].setAttribute('type','text')
      }
      inputs = document.querySelectorAll('input[type^="text"');
      for (i = 0; i < inputs.length; i++) {
          inputs[i].style.width="100%";
      }
    }
  }

  function reset() {
    console.log("reset?");
  }

  browser.runtime.onMessage.addListener((message) => {
    if (message.command === "cmd") {
      doAction(message.action);
    } else if (message.command === "reset") {
      reset();
    }
  });

})();
