package org.softlang.company;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.BooleanWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.WritableComparable;

/**
 * An employee has a salary and some person information
 * 
 */
public class Employee implements WritableComparable<Employee> {

	private Text name;
	private Text address;
	private DoubleWritable salary;
	private Text company;
	private Text department;
	private BooleanWritable isManager = new BooleanWritable(false);

	public Text getName() {
		return name;
	}

	public void setName(Text name) {
		this.name = name;
	}

	public void setName(String name) {
		if (this.name == null)
			this.name = new Text();
		this.name.set(name);
	}

	public Text getAddress() {
		return address;
	}

	public void setAddress(Text address) {
		this.address = address;
	}

	public void setAddress(String address) {
		if (this.address == null)
			this.address = new Text();
		this.address.set(address);
	}

	public Text getCompany() {
		return company;
	}

	public void setCompany(Text company) {
		this.company = company;
	}

	public DoubleWritable getSalary() {
		return salary;
	}

	public void setSalary(DoubleWritable salary) {
		this.salary = salary;
	}

	public void setSalary(double salary) {
		if (this.salary == null)
			this.salary = new DoubleWritable();
		this.salary.set(salary);
	}

	public Text getDepartment() {
		return department;
	}

	public void setDepartment(Text department) {
		this.department = department;
	}

	public BooleanWritable isManager() {
		return isManager;
	}

	public void setManager(BooleanWritable isManager) {
		this.isManager = isManager;
	}

	public void setManager(boolean isManager) {
		if (this.isManager == null)
			this.isManager = new BooleanWritable();
		this.isManager.set(isManager);
	}

	/**
	 * Read (say, deserialize) an employee
	 */
	@Override
	public void readFields(DataInput in) throws IOException {
		name = new Text();
		name.readFields(in);
		address = new Text();
		address.readFields(in);
		company = new Text();
		company.readFields(in);
		salary = new DoubleWritable();
		salary.readFields(in);
		department = new Text();
		department.readFields(in);
		isManager = new BooleanWritable();
		isManager.readFields(in);
	}

	/**
	 * Write (say, serialize) an employee.
	 */
	@Override
	public void write(DataOutput out) throws IOException {
		name.write(out);
		address.write(out);
		company.write(out);
		salary.write(out);
		department.write(out);
		isManager.write(out);

	}

	@Override
	public int compareTo(Employee that) {
		if (that.name.compareTo(this.name) != 0)
			return (that.name.compareTo(this.name)) > 0 ? 1 : -1;
		if (that.address.compareTo(this.address) != 0)
			return that.address.compareTo(this.address);
		if (that.company.compareTo(this.company) != 0)
			return that.company.compareTo(this.company);
		if (that.salary.compareTo(this.salary) != 0)
			return that.salary.compareTo(this.salary) > 0 ? 1 : -1;
		if (that.department.compareTo(this.department) != 0)
			return that.department.compareTo(this.department) > 0 ? 1 : -1;
		if (that.isManager.compareTo(this.isManager) != 0)
			return that.isManager.compareTo(this.isManager) > 0 ? 1 : -1;

		return 0;
	}
}
