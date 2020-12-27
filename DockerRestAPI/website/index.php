<html>
    <head>
        <title>CIS 322 REST-api demo: Control Times</title>
    </head>

    <body>
        <h1>List All</h1>
            <?php
            $json = file_get_contents("http://laptop-service/listAll");
            $obj = json_decode($json);
                $open = $obj->open_time;
                $close = $obj->close_time;
            echo "Open Times are: \n";
            foreach ($open as $l) {
                echo "<li>$l</li>";
            }
            echo "Close Times are: \n";
            foreach ($close as $l) {
                echo "<li>$l</li>";
            }
            ?>

        <h1>List All JSON</h1>
        <?php
            $json = file_get_contents("http://laptop-service/listAll/json");
            $obj = json_decode($json);
                $open = $obj->open_time;
                $close = $obj->close_time;
            echo "Open Times are: \n";
            foreach ($open as $l) {
                echo "<li>$l</li>";
            }
            echo "Close Times are: \n";
            foreach ($close as $l) {
                echo "<li>$l</li>";
            }
            ?>

        <h1>List All CSV</h1>
        <?php
        echo "List all in csv format: \n";
        echo file_get_contents('http://laptop-service/listAll/csv');
        ?>

        <h1>List Open Only</h1>
        <?php
        $json = file_get_contents("http://laptop-service/listOpenOnly");
        $obj = json_decode($json);
            $open = $obj->open_time;
        echo "Open Times are: \n";
            foreach ($open as $l) {
                echo "<li>$l</li>";
            }
        ?>

        <h1>List Open Only JSON</h1>
        <?php
        $json = file_get_contents("http://laptop-service/listOpenOnly/json");
        $obj = json_decode($json);
            $open = $obj->open_time;
        echo "Open Times are: \n";
            foreach ($open as $l) {
                echo "<li>$l</li>";
            }
        ?>

        <h1>List Open Only CSV</h1>
        <?php
        echo "List open in csv format: \n";
        echo file_get_contents('http://laptop-service/listOpenOnly/csv');
        ?>

        <h1>List Close Only</h1>
        <?php
        $json = file_get_contents("http://laptop-service/listCloseOnly");
        $obj = json_decode($json);
            $close = $obj->close_time;
        echo "Close Times are: \n";
            foreach ($close as $l) {
                echo "<li>$l</li>";
            }
        ?>

        <h1>List Close Only JSON</h1>
        <?php
        $json = file_get_contents("http://laptop-service/listCloseOnly/json");
        $obj = json_decode($json);
            $close = $obj->close_time;
        echo "Close Times are: \n";
            foreach ($close as $l) {
                echo "<li>$l</li>";
            }
        ?>

        <h1>List Close Only CSV</h1>
        <?php
        echo "List close in csv format: \n";
        echo file_get_contents('http://laptop-service/listCloseOnly/csv');
        ?>

    </body>
</html>
