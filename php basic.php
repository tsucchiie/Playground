<?php

//------------------------------------------------------------
                            //PRINTING
$nama = 'Arindra';
$nim = 'L20019065';

echo $nama , $nim;
echo 'nama saya ', $nama ,' nim ', $nim;

echo "<marquee style='color:red's>duerbfrkfblufrbefbvfbflfbklefbekfb lerbfv2vf2ruvfi2u3fv2iyfv2;yvf72rf7f"

//------------------------------------------------------------
                            //IF ELSE
if($fossclass != "Sabtu" && $ngobar == "Kamis"){
	echo " Hari ini tidak Fossclass tapi Ngobar ";
}elseif($fossclass == "Sabtu" && $ngobar != "Kamis"){
	echo " Hari ini Fossclass tapi tidak Ngobar ";
}elseif($fossclass == "Sabtu" && $ngobar == "Kamis"){
	echo " Hari ini Fossclass dan Ngobar ";
}else{
	echo "Hari ini tidak Fossclass dan tidak Ngobar";
}
$fossclass = "Sabtu";
$ngobar = "Kamis";


//-------------------------------------------------------------
                            //FUNCTION

function tampilkan_nama(){
    echo "Arindra Hning";
    }
    
    tampilkan_nama();

//--------------------------------------------------------------
                            //LOOPING

for($x=1;$x<=10;$x++){
	echo $x;}                        

//--------------------------------------------------------------
                            //ARRAY

//membuat array yang berisi nama buah-buahan
$buah = array('semangka','jeruk','apel','anggur');
//menampilkan data array dengan nomor urut 2
echo $buah[2];

//---------------------------------------------------------------
                            //ARRAY DG NAMA

//penamaan isi array
$buah['semangka'] = "isinya merah";
$buah['jeruk'] = "rasanya manis";
$buah['apel'] = "warnanya merah";
$buah['anggur'] = "harganya mahal";

// menampilkan isi array yang bernama jeruk
echo $buah['jeruk'];


//--- PART2 ---


$buah = array(
	'semangka' => "isinya merah",
	'jeruk' => "rasanya manis",
	'apel' => "warnanya merah",
	'anggur' => "harganya mahal"
);

// menampilkan isi array yang bernama jeruk
echo $buah['jeruk'];


?>