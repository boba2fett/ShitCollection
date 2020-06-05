<!DOCTYPE html>
<html>
<body>

    <form name="uploadformular" enctype="multipart/form-data" action="upload.php" method="post">
    Datei: <input type="file" name="uploaddatei" size="1024" maxlength="255">
    <input type="Submit" name="submit" value="Datei hochladen">
    </form>

</body>
</html>
<?php
error_reporting(E_ALL);
    echo "<pre>";
    echo "FILES:<br>";/home/mypc/git/p0wny-shell/logp0wny.php
    print_r ($_FILES );
    echo "</pre>";
    if ( $_FILES['uploaddatei']['name']  <> "" )
    {/home/mypc/git/p0wny-shell/logp0wny.php
            $_FILES['uploaddatei']['name'] = dateiname_bereinigen($_FILES['uploaddatei']['name']);
    
            if ( $_FILES['uploaddatei']['name'] <> '')
            {
                $time=time();
                $datum = date('Y').'-'.date('m').'-'.date('d');
                $dir='/var/www/html/upload/'.$datum.'/';
                mkdir($dir);
                $movename=$dir.$_FILES['uploaddatei']['name'].'.b2f.'.$time;
                $websPath='/upload/'.$datum.'/'.$_FILES['uploaddatei']['name'].'.b2f.'.$time;
                $status=move_uploaded_file($_FILES['uploaddatei']['tmp_name'],$movename);
                    echo "<p>status=".$status."</p>";
                    echo "<p>Hochladen war erfolgreich: ";
                    echo '<a href="'.$websPath.'">';
                    echo $_FILES['uploaddatei']['name'];
                    echo '</a></p>';
            }
            else
            {
                echo "<p>Dateiname ist nicht zulässig</p>";
            }
    }

function dateiname_bereinigen($dateiname)
    {

        $dateiname = str_replace(' ', '-', $dateiname);
        
        $dateiname = strtolower ( $dateiname );
        $dateiname = str_replace ('"', "-", $dateiname );
        $dateiname = str_replace ("'", "-", $dateiname );
        $dateiname = str_replace ("*", "-", $dateiname );
        $dateiname = str_replace ("ß", "ss", $dateiname );
        $dateiname = str_replace ("ß", "ss", $dateiname );
        $dateiname = str_replace ("ä", "ae", $dateiname );
        $dateiname = str_replace ("ä", "ae", $dateiname );
        $dateiname = str_replace ("ö", "oe", $dateiname );
        $dateiname = str_replace ("ö", "oe", $dateiname );
        $dateiname = str_replace ("ü", "ue", $dateiname );
        $dateiname = str_replace ("ü", "ue", $dateiname );
        $dateiname = str_replace ("Ä", "ae", $dateiname );
        $dateiname = str_replace ("Ö", "oe", $dateiname );
        $dateiname = str_replace ("Ü", "ue", $dateiname );
        $dateiname = htmlentities ( $dateiname );
        $dateiname = str_replace ("&", "und", $dateiname );
        $dateiname = str_replace ("+", "und", $dateiname );
        $dateiname = str_replace ("(", "-", $dateiname );
        $dateiname = str_replace (")", "-", $dateiname );
        $dateiname = str_replace (" ", "-", $dateiname );
        $dateiname = str_replace ("\'", "-", $dateiname );
        $dateiname = str_replace ("/", "-", $dateiname );
        $dateiname = str_replace ("?", "-", $dateiname );
        $dateiname = str_replace ("!", "-", $dateiname );
        $dateiname = str_replace (":", "-", $dateiname );
        $dateiname = str_replace (";", "-", $dateiname );
        $dateiname = str_replace (",", "-", $dateiname );
        $dateiname = str_replace ("--", "-", $dateiname );
    
        $dateiname = filter_var($dateiname, FILTER_SANITIZE_URL);

        $dateiname = preg_replace('/[^A-Za-z0-9\-]/', '', $dateiname);
        

        return ($dateiname);
    }
    
?>
