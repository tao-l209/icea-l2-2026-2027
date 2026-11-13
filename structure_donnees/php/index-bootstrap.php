<?php
// index-bootstrap.php
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>MyWebsite - Bootstrap</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

    <!-- HEADER -->
    <header class="bg-dark text-white p-3">

        <div class="container-fluid">

            <div class="d-flex align-items-center justify-content-between flex-wrap gap-3">

                <!-- SITE NAME -->
                <div>
                    <a href="#" class="text-white text-decoration-none fs-3 fw-bold">
                        MyWebsite
                    </a>
                </div>

                <!-- NAVIGATION -->
                <nav>
                    <ul class="nav">
                        <li class="nav-item">
                            <a href="#" class="nav-link text-white">Home</a>
                        </li>

                        <li class="nav-item">
                            <a href="#" class="nav-link text-white">About</a>
                        </li>

                        <li class="nav-item">
                            <a href="#" class="nav-link text-white">Services</a>
                        </li>

                        <li class="nav-item">
                            <a href="#" class="nav-link text-white">Contact</a>
                        </li>
                    </ul>
                </nav>

                <!-- LOGIN / PASSWORD -->
                <div>
                    <form class="d-flex flex-wrap gap-2">

                        <input
                            type="text"
                            class="form-control"
                            placeholder="Login"
                            style="width: 130px;"
                        >

                        <input
                            type="password"
                            class="form-control"
                            placeholder="Password"
                            style="width: 130px;"
                        >

                        <button type="button" class="btn btn-primary">
                            Login
                        </button>

                    </form>
                </div>

                <!-- LANGUAGE -->
                <div>
                    <select class="form-select">
                        <option selected>FR</option>
                        <option>EN</option>
                        <option>ES</option>
                    </select>
                </div>

            </div>

        </div>

    </header>


    <!-- MAIN CONTAINER -->
    <div class="container-fluid py-4">

        <div class="row g-4">

            <!-- CONTENT -->
            <main class="col-md-8">

                <div class="bg-white p-4 rounded shadow-sm">

                    <h2>CONTENT</h2>

                    <p>
                        Welcome to MyWebsite.
                        This is the main content section.
                    </p>

                </div>

            </main>


            <!-- ASIDE -->
            <aside class="col-md-4">

                <div class="bg-white p-4 rounded shadow-sm">

                    <h2>ASIDE</h2>

                    <p>
                        Additional information goes here.
                    </p>

                </div>

            </aside>

        </div>

    </div>


    <!-- FOOTER -->
    <footer class="bg-dark text-white text-center p-4 mt-4">

        <p class="mb-0">
            © 2026 MyWebsite - All rights reserved.
        </p>

    </footer>

</body>
</html>