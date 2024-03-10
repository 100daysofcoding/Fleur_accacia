package figure;

public abstract class Forme {
    private String nom;

//    public Forme();

    public Forme(String nom) {
        this.nom = nom;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public abstract double aire();


    @Override
    public String toString() {
        return "Forme{" +
                "nom='" + nom + '\'' +
                '}';
    }
}
