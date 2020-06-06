<!DOCTYPE html>
<html>
<body>

    <form name="uploadformular" enctype="multipart/form-data" action="upload.php" method="post">
    Datei: <input type="file" name="uploadfile" size="1024" maxlength="255">
    <input type="Submit" name="submit" value="Upload File">
    </form>

</body>
</html>
<?php
error_reporting(E_ALL);
    echo "<pre>";
    echo "FILES:<br>";
    print_r ($_FILES );
    echo "</pre>";
    if ( $_FILES['uploadfile']['name']  <> "" )
    {
            $_FILES['uploadfile']['name'] = dateiname_bereinigen($_FILES['uploadfile']['name']);
    
            if ( $_FILES['uploadfile']['name'] <> '')
            {
                $time=time();
                $datum = date('Y').'-'.date('m').'-'.date('d');
                $dir='/var/www/html/upload/'.$datum.'/';
                mkdir($dir);
                $movename=$dir.$_FILES['uploadfile']['name'].'.b2f.'.$time;
                $websPath='/upload/'.$datum.'/'.$_FILES['uploadfile']['name'].'.b2f.'.$time;
                $status=move_uploaded_file($_FILES['uploadfile']['tmp_name'],$movename);
                    echo "<p>status=".$status."</p>";
                    echo "<p>Hochladen war erfolgreich: ";
                    echo '<a href="'.$websPath.'">';
                    echo $_FILES['uploadfile']['name'];
                    echo '</a></p>';
            }
            else
            {
                echo "<p>Filename not valid</p>";
            }
    }

function dateiname_bereinigen($filename)
    {

        $filename = str_replace(' ', '-', $filename);
        
        $filename = strtolower ( $filename );
        $filename = str_replace ('"', "-", $filename );
        $filename = str_replace ("'", "-", $filename );
        $filename = str_replace ("*", "-", $filename );
        $filename = str_replace ("ß", "ss", $filename );
        $filename = str_replace ("ß", "ss", $filename );
        $filename = str_replace ("ä", "ae", $filename );
        $filename = str_replace ("ä", "ae", $filename );
        $filename = str_replace ("ö", "oe", $filename );
        $filename = str_replace ("ö", "oe", $filename );
        $filename = str_replace ("ü", "ue", $filename );
        $filename = str_replace ("ü", "ue", $filename );
        $filename = str_replace ("Ä", "ae", $filename );
        $filename = str_replace ("Ö", "oe", $filename );
        $filename = str_replace ("Ü", "ue", $filename );
        $filename = htmlentities ( $filename );
        $filename = str_replace ("&", "und", $filename );
        $filename = str_replace ("+", "und", $filename );
        $filename = str_replace ("(", "-", $filename );
        $filename = str_replace (")", "-", $filename );
        $filename = str_replace (" ", "-", $filename );
        $filename = str_replace ("\'", "-", $filename );
        $filename = str_replace ("/", "-", $filename );
        $filename = str_replace ("?", "-", $filename );
        $filename = str_replace ("!", "-", $filename );
        $filename = str_replace (":", "-", $filename );
        $filename = str_replace (";", "-", $filename );
        $filename = str_replace (",", "-", $filename );
        $filename = str_replace ("--", "-", $filename );
    
        $filename = filter_var($filename, FILTER_SANITIZE_URL);

        $filename = preg_replace('/[^A-Za-z0-9\-]/', '', $filename);
        

        return ($filename);
    }
    
?>
