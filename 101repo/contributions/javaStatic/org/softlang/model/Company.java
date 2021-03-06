package org.softlang.model;

import java.io.Serializable;
import java.util.LinkedList;
import java.util.List;

/**
 * A company has a name and consists of (possibly nested) departments.
 */
public class Company implements Serializable {

	private static final long serialVersionUID = -200889592677165250L;

	private String name;
	private List<Department> depts = new LinkedList<Department>();

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<Department> getDepts() {
		return depts;
	}
}
