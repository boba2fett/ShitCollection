function listenForClicks() {
  document.addEventListener("click", (e) => {

    function execute(tabs) {
      let cmd = e.target.textContent;
      browser.tabs.sendMessage(tabs[0].id, {
        command: "cmd",
        action: cmd
      });
      window.close();
    }

    function reportError(error) {
      console.error(`Error: ${error}`);
    }

    if (e.target.classList.contains("action")) {
      browser.tabs.query({active: true, currentWindow: true})
        .then(execute)
        .catch(reportError);
    }
  });
}
function reportExecuteScriptError(error) {
  document.querySelector("#popup-content").classList.add("hidden");
  document.querySelector("#error-content").classList.remove("hidden");
  console.error(`Failed to execute execute content script: ${error.message}`);
}
browser.tabs.executeScript({file: "/content_scripts/execute.js"})
.then(listenForClicks)
.catch(reportExecuteScriptError);
