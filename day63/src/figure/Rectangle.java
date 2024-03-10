package figure;

public class Rectangle extends Forme{
    private double longueur;
    private double largeur;

    public Rectangle(String nom,double longueur, double largeur){
        super(nom);
        this.longueur = longueur;
        this.largeur = largeur;
    }

    public double getLongueur() {
        return longueur;
    }

    public void setLongueur(double longueur) {
        this.longueur = longueur;
    }

    public double getLargeur() {
        return largeur;
    }

    public void setLargeur(double largeur) {
        this.largeur = largeur;
    }

    @Override
    public double aire() {
        return (largeur*longueur);
    }
}
