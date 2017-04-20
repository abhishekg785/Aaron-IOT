public class Display {

	String fname;
	String lname;

	public Display(String fname, String lname) {
		System.out.println("in the Display cons");
		this.fname = fname;
		this.lname = lname;
		this.showData();
		//Display obj = new Display("abhishek", "goswami");
		
	}
	
	public void showData() {
		System.out.println("showing data");
		System.out.println("The name is" + this.fname + " " + this.lname);
		this.demoFunc();
	}

	public void demoFunc() {
		System.out.println("IN THE DEMO FUNCTION");
	}

	public static void main(String args[]) {
		System.out.println("hello i am in main function");
		Display obj = new Display("abhishek", "goswami");
	}
}


