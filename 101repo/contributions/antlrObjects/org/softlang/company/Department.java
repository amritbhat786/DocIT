package org.softlang.company;

import java.util.LinkedList;
import java.util.List;

/**
 * A department has a name, a manager, employees, and subdepartments.
 */
public class Department {

	private String name;
	private Employee manager;
	private List<Department> subdepts;
	private List<Employee> employees;

	public Department() {
		subdepts = new LinkedList<Department>();
		employees = new LinkedList<Employee>();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Employee getManager() {
		return manager;
	}

	public void setManager(Employee manager) {
		this.manager = manager;
	}

	public List<Department> getSubdepts() {
		return subdepts;
	}

	public List<Employee> getEmployees() {
		return employees;
	}
	
	public double total() {
		double total = 0;
		total += getManager().getSalary();
		for (Department s : getSubdepts())
			total += s.total();
		for (Employee e : getEmployees())
			total += e.getSalary();
		return total;		
	}	
	
	public void cut() {
		getManager().cut();
		for (Department s : getSubdepts())
			s.cut();
		for (Employee e : getEmployees())
			e.cut();
	}		
}
