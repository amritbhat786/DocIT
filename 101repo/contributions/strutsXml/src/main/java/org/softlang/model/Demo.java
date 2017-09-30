package org.softlang.model;

public class Demo {

	public Company createCompany() {
		Company company = new Company();

		company.setName("meganalysis");

		Person craig = new Person();
		craig.setName("Craig");
		craig.setAddress("Redmond");
		Person erik = new Person();
		erik.setName("Erik");
		erik.setAddress("Utrecht");
		Person ralf = new Person();
		ralf.setName("Ralf");
		ralf.setAddress("Koblenz");
		Person ray = new Person();
		ray.setName("Ray");
		ray.setAddress("Redmond");
		Person klaus = new Person();
		klaus.setName("Klaus");
		klaus.setAddress("Boston");
		Person karl = new Person();
		karl.setName("Karl");
		karl.setAddress("Riga");
		Person joe = new Person();
		joe.setName("Joe");
		joe.setAddress("Wifi City");

		Employee CraigE = new Employee();
		Employee erikE = new Employee();
		Employee ralfE = new Employee();
		Employee rayE = new Employee();
		Employee klausE = new Employee();
		Employee karlE = new Employee();
		Employee joeE = new Employee();

		CraigE.setPerson(craig);
		erikE.setPerson(erik);
		ralfE.setPerson(ralf);
		rayE.setPerson(ray);
		klausE.setPerson(klaus);
		karlE.setPerson(karl);
		joeE.setPerson(joe);

		CraigE.setSalary(123456);
		erikE.setSalary(12345);
		ralfE.setSalary(1234);
		rayE.setSalary(234567);
		klausE.setSalary(23456);
		karlE.setSalary(2345);
		joeE.setSalary(2344);

		Dept research = new Dept();
		

		research.setManager(CraigE);
		research.setName("Research");
		research.getSubunits().add(erikE);
		research.getSubunits().add(ralfE);

		Dept development = new Dept();
		development.setManager(rayE);
		development.setName("Development");
		
		Dept dev1 = new Dept();
		dev1.setName("Dev1");
		dev1.setManager(klausE);
		
		Dept dev11 = new Dept();
		dev11.setName("Dev1.1");
		dev11.setManager(karlE);
		
		development.getSubunits().add(dev1);
		
		dev1.getSubunits().add(dev11);
	
		dev11.getSubunits().add(joeE);

		company.getDepts().add(research);
		company.getDepts().add(development);

		return company;
	}
}
