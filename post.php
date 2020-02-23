// Phone_Number v1.0.1 
// coded by: hack4lx
// 👊 ʍ4ղíƒҽՏԵ0 ϲվҍҽɾ ՏҽϲմɾíԵվ Եҽɑʍ™💪
// Thank You :  @rainboy1 | @KindKhers4lx | @Mohsening | @Vampire4lx | @erfan4lx | @HatBLACK4LX
<?php
$json = (file_get_contents('php://input'));
$dejson = json_decode($json, true);
$location = $dejson['data'];
shell_exec("python3 send.py ".$location);
?>
