//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:11:07 PM CEST 
//


package model.api.corporation.membertracking;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element ref="{}rowset"/>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "rowset"
})
@XmlRootElement(name = "result")
public class Result {

    @XmlElement(required = true)
    protected Rowset rowset;

    /**
     * Gets the value of the rowset property.
     * 
     * @return
     *     possible object is
     *     {@link Rowset }
     *     
     */
    public Rowset getRowset() {
        return rowset;
    }

    /**
     * Sets the value of the rowset property.
     * 
     * @param value
     *     allowed object is
     *     {@link Rowset }
     *     
     */
    public void setRowset(Rowset value) {
        this.rowset = value;
    }

}
