//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:11:15 PM CEST 
//


package model.api.eve.factionalwarfaretopstats;

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
 *         &lt;element ref="{}characters"/>
 *         &lt;element ref="{}corporations"/>
 *         &lt;element ref="{}factions"/>
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
    "characters",
    "corporations",
    "factions"
})
@XmlRootElement(name = "result")
public class Result {

    @XmlElement(required = true)
    protected Characters characters;
    @XmlElement(required = true)
    protected Corporations corporations;
    @XmlElement(required = true)
    protected Factions factions;

    /**
     * Gets the value of the characters property.
     * 
     * @return
     *     possible object is
     *     {@link Characters }
     *     
     */
    public Characters getCharacters() {
        return characters;
    }

    /**
     * Sets the value of the characters property.
     * 
     * @param value
     *     allowed object is
     *     {@link Characters }
     *     
     */
    public void setCharacters(Characters value) {
        this.characters = value;
    }

    /**
     * Gets the value of the corporations property.
     * 
     * @return
     *     possible object is
     *     {@link Corporations }
     *     
     */
    public Corporations getCorporations() {
        return corporations;
    }

    /**
     * Sets the value of the corporations property.
     * 
     * @param value
     *     allowed object is
     *     {@link Corporations }
     *     
     */
    public void setCorporations(Corporations value) {
        this.corporations = value;
    }

    /**
     * Gets the value of the factions property.
     * 
     * @return
     *     possible object is
     *     {@link Factions }
     *     
     */
    public Factions getFactions() {
        return factions;
    }

    /**
     * Sets the value of the factions property.
     * 
     * @param value
     *     allowed object is
     *     {@link Factions }
     *     
     */
    public void setFactions(Factions value) {
        this.factions = value;
    }

}
