<?php
    header('Content-type:application/json; charset=utf-8');

    $title= $_POST['title'];
    $message= $_POST['msg'];

    $response= [];
    $response['title']= $title;
    $response['msg']= $message;

    //echo json_encode($response)
    echo json_encode($response, JSON_UNESCAPED_UNICODE) # 이 옵션 없으면 데이터 깨짐. 보낼때부터 이미 utf-8로 된 데이터 여서.
?>