<?php
    //create user 
    $con=mysqli_connect("localhost","root", null, "icea-l2-2026-2027");
    for ($i = 0; $i < 3; $i++) {
        $sql="INSERT INTO users VALUES ($i,'user','password',1)";
        if (mysqli_query($con,$sql))
        {
        echo "It Works";
        }
        else
        {
        echo "Nope";
        }
    }
    
?>