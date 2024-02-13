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
    private List<String> repas;
    
  
    
    public Restaurant(){  
    }  
    public Restaurant(String nom, int star, String repas){
        this.nom= nom;
        this.star= star;
        this.repas = new ArrayList<>();
        
    }

    public void description() {
        System.out.println("Le restaurant " + nom + ", est un restaurant " +star +" étoiles");
    }
    public void servir(){
       System.out.println("Le restaurant " + nom + " sert plusieurs repas : " + repas);
    }
    
    public String getNom(){
        return nom;        
    }
    public void setNom(String n){
        this.nom = n;
    }

    public void ajouterRepas(String repas) {
        this.repas.add(repas);
    }
   
    @Override
    public String toString(){
        return "le resto "+nom+" pour vous servir.";
    }  
    
}




