function Display() {
	this.fname = 'abhishek';
	this.lname = 'goswami';
	this.display = function() {
		console.log(this.fname + ' ' + this.lname);
	}
}


obj = new Display()
obj.display()
