package figure;

public class Triangle extends Forme {
    private double base;
    private double hauteur;

    public Triangle(String nom,double base, double hauteur) {
        super(nom);
        this.base = base;
        this.hauteur = hauteur;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
    }

    public double getHauteur() {
        return hauteur;
    }

    public void setHauteur(double hauteur) {
        this.hauteur = hauteur;
    }

    @Override
    public double aire() {
        return (base*hauteur)/2;
    }
}



