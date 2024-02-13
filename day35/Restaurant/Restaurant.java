/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package restaurant;

/**
 *
 * @author user
 */
public class Restaurant {
    private String nom;
    protected int star;
    private String repas;
    
    public Restaurant(){  
    }  
    public Restaurant(String nom, int star, String repas){
        this.nom= nom;
        this.star= star;
        this.repas = repas;
    }
    
    public void servir(){
        System.out.println("Le resto "+nom+" avec "+star+"étoiles sert plusieurs "+repas);
    }
    
    public String getNom(){
        return nom;        
    }
    public void setNom(String n){
        this.nom = n;
    }
     public String getRepas(){
        return repas;        
    }
    public void setRepas(String repas){
        this.repas = repas;
    }
   
    @Override
    public String toString(){
        return "le resto "+nom+" pour vous servir.";
    }  
    
}




