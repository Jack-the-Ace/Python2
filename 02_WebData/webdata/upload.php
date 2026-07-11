<?php
    header('Content-type:text/plain; charset=utf-8');

    $title= $_POST['title'];
    $message= $_POST['msg'];

    if (!isset($_FILES['img'])) {
        echo "파일이 없습니다 \n";
        exit;
    }

    $file = $_FILES['img'];
    $file_name= $file['name'];
    $temp_name= $file['tmp_name'];

    $upload_dir = './uploads/';
    $dst_name = $upload_dir . date('Ymd') . $file_name;

    if (move_uploaded_file($temp_name, $dst_name)) echo "업로드 성공 \n";
    else echo "업로드 실패 \n";

    echo "$title \n";
    echo "$message";
    
?>