const mahasiswa = { nama:"Ucup", umur:12, universitas:"ITB", disabilitas:"wibu" };

const rumah = {
	lokasi:"Jakarta",
	harga:120000,
	printInfo: function printInfo(lokasi, harga)
	{
		console.log(lokasi, harga);
	} 
};

let a = mahasiswa.nama;

let b = rumah["harga"];

let c = new mahasiswa();

rumah.printInfo("Bandung", 15000);

