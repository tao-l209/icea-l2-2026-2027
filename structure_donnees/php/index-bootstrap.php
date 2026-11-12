<?php
// index-bootstrap.php
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Web Layout - Bootstrap</title>

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <!-- HEADER -->
    <header class="bg-dark text-white text-center p-4">
        <h1>HEADER</h1>
    </header>

    <!-- MAIN CONTAINER -->
    <div class="container-fluid">
        <div class="row min-vh-100">

            <!-- NAVIGATION -->
            <nav class="col-md-3 col-lg-2 bg-light p-4">
                <h2>NAV</h2>

                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link 1</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link 2</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link 3</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link 4</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link 5</a>
                    </li>
                </ul>
            </nav>

            <!-- CONTENT -->
            <main class="col-md-6 col-lg-8 bg-white p-4">
                <h2>CONTENT</h2>
            </main>

            <!-- ASIDE -->
            <aside class="col-md-3 col-lg-2 bg-light p-4">
                <h2>ASIDE</h2>
            </aside>

        </div>
    </div>

    <!-- FOOTER -->
    <footer class="bg-dark text-white text-center p-4">
        <h2>FOOTER</h2>
    </footer>

    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

    <script src="js/script.js"></script>

</body>
</html>
