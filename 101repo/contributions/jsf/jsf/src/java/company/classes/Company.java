package company.classes;
// Generated 26.10.2011 15:04:34 by Hibernate Tools 3.2.1.GA

import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import static javax.persistence.GenerationType.IDENTITY;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.persistence.UniqueConstraint;

/**
 * Company generated by hbm2java
 */
@Entity
@Table(name="company",
    catalog="test",
    uniqueConstraints = @UniqueConstraint(columnNames="name") 
)
public class Company implements Serializable {

    private Long id;
    private String name;
    private Set<Department> departments = new HashSet<Department>(0);
    private Set<Employee> employees = new HashSet<Employee>(0);

    public Company() {}
	
    public Company(String name) {
        this.name = name;
    }
    public Company(String name, Set<Department> departments, Set<Employee> employees) {
       this.name = name;
       this.departments = departments;
       this.employees = employees;
    }
   
    @Id
    @GeneratedValue(strategy=IDENTITY)
    @Column(name="id", unique=true, nullable=false)
    public Long getId() {
        return this.id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    @Column(name="name", unique=true, nullable=false, length=100)
    public String getName() {
        return this.name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    @OneToMany(cascade=CascadeType.ALL, fetch=FetchType.LAZY, mappedBy="company")
    public Set<Department> getDepartments() {
        return this.departments;
    }
    
    public void setDepartments(Set<Department> departments) {
        this.departments = departments;
    }
    
    @OneToMany(cascade=CascadeType.ALL, fetch=FetchType.EAGER, mappedBy="company")
    public Set<Employee> getEmployees() {
        return this.employees;
    }
    
    public void setEmployees(Set<Employee> employees) {
        this.employees = employees;
    }




}


