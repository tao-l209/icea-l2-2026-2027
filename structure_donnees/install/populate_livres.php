<?php

    $connexion = new mysqli("localhost", "root", "");
        $connexion->select_db("icea-l2-structure-donnee");

?>



<HTML>
    <BODY> 
         <DIV align="center">

          <form method="post" action="<?php $_SERVER["PHP_SELF"] ?>" enctype="multipart/form-data" style="width:500px">
                <fieldset>
                    <legend>Ajouter un Livre </legend>
                    <div ><label>Titre :</label>&nbsp;<input type="text" name="nom" maxlength="30" value="" /></div>
                    <div ><label>ISBN:</label>&nbsp;<input type="bigint" name="code" value="" /></div>
                    <br/><br/>
                    <div>
                        <input type="hidden" name="MAX_FILE_SIZE" value="3000000" />
                        <input type="submit" value="Soumettre" />
                    </div>
                </fieldset>
            </form>
        </DIV>
    </BODY>
</HTML>
<?php
    

    if(isset($_POST["nom"]))
        {
            // récupération de nos données si le formulaire a été soumis
            $nom = $connexion->escape_string($_POST["nom"]);
            $ISBN = $connexion->escape_string($_POST["code"]);
        
            if(!empty($nom) && sizeof($ISBN) != 0)
            {   

                $ligne_inserees = 0;
                $ligne_attendues = 0;
                $connexion->autocommit(TRUE);

                $requete = "INSERT INTO Livres (Titre,ISBN) VALUES( '$nom', '$ISBN' );";
                $resultat = $connexion->query($requete);

            }
        }
?>