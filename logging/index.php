<html>
<?php
$format = "csv"; //Moeglichkeiten: csv und txt

$datum_zeit = date("d.m.Y H:i:s");
$ip = $_SERVER["REMOTE_ADDR"];
$site = $_SERVER['REQUEST_URI'];
$browser = $_SERVER["HTTP_USER_AGENT"];

$monate = array(1=>"Januar", 2=>"Februar", 3=>"Maerz", 4=>"April", 5=>"Mai", 6=>"Juni", 7=>"Juli", 8=>"August", 9=>"September", 10=>"Oktober", 11=>"November", 12=>"Dezember");
$monat = date("n");
$jahr = date("y");

$dateiname="log-index/log_".$monate[$monat]."_$jahr.$format";

$header = array("Datum", "IP", "Seite", "Browser");
$infos = array($datum_zeit, $ip, $site, $browser);

if($format == "csv")
{
    $eintrag= '"'.implode('", "', $infos).'"';
}
else 
{
    $eintrag = implode("\t", $infos);
}

$write_header = !file_exists($dateiname);

$datei=fopen($dateiname,"a");

if($write_header) 
{
    if($format == "csv")
    {
        $header_line = '"'.implode('", "', $header).'"';
    }
    else
    {
        $header_line = implode("\t", $header);
    }
    fputs($datei, $header_line."\n");
}
fputs($datei,$eintrag."\n");
fclose($datei);
?>

<script  type="text/javascript">
window.onload = function () 
{
logging();
};

function logging()
{
    post("indexForward.php", { screenX: screen.width, screenY:screen.height, windowX:window.innerWidth, windowY: window.innerHeight});
};

function post(path, params, method="post") 
{
  // The rest of this code assumes you are not using a library.
  // It can be made less wordy if you use one.
  const form = document.createElement("form");
  form.method = method;
  form.action = path;
  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const hiddenField = document.createElement("input");
      hiddenField.type = "hidden";
      hiddenField.name = key;
      hiddenField.value = params[key];

      form.appendChild(hiddenField);
    }
  }
  document.body.appendChild(form);
  form.submit();
};

</script>

<noscript>
Bitte aktivieren Sie javascript
</noscript>
</html>

