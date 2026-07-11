<?php
    header('Content-type:text/plain; charset=utf-8');

    $title= $_GET['title'];
    $message= $_GET['msg'];

    echo "제목: $title \n";
    echo "메세지: $message";
?>