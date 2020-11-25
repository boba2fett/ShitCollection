function listenForClicks() {
  document.addEventListener("click", (e) => {

    function execute(tabs) {
      let cmd = e.target.textContent;
      browser.tabs.sendMessage(tabs[0].id, {
        command: "cmd",
        action: cmd
      });
    }

    function reset(tabs) {
      browser.tabs.sendMessage(tabs[0].id, {
          command: "reset",
        });
    }

    function reportError(error) {
      console.error(`Error: ${error}`);
    }

    if (e.target.classList.contains("action")) {
      browser.tabs.query({active: true, currentWindow: true})
        .then(execute)
        .catch(reportError);
    }
    else if (e.target.classList.contains("reset")) {
      browser.tabs.query({active: true, currentWindow: true})
        .then(reset)
        .catch(reportError);
    }
  });
}
function reportExecuteScriptError(error) {
  document.querySelector("#popup-content").classList.add("hidden");
  document.querySelector("#error-content").classList.remove("hidden");
  console.error(`Failed to execute execute content script: ${error.message}`);
}

function updatePopup(restoredSettings) {
  document.querySelector("#stored").innerHTML = restoredSettings.stored.text || "";
}

const gettingStoredSettings = browser.storage.local.get();
gettingStoredSettings.then(updatePopup, reportExecuteScriptError);

browser.tabs.executeScript({file: "/content_scripts/execute.js"})
.then(listenForClicks)
.catch(reportExecuteScriptError);
