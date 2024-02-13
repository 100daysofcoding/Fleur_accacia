/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package restaurant;

/**
 *
 * @author user
 */
public class FastFood extends Restaurant{
    private int time;
    
    public FastFood(int T,String nom, int star, String repas){ 
        super(nom,star,repas);
        this.time =T;
    }
    public void preparer(){
        System.out.println("Le fastfood "+super.getNom()+" prepare le "+super.getRepas()+" en "+time+" minutes");
    }
    
    public int getTime(){
        return time;
    }
    public void setTime(int time){
        this.time= time;
    }

    @Override
    public String toString(){
        return "le FastFood "+super.getNom()+" est ouvert 24h/24.";
    }  

}
