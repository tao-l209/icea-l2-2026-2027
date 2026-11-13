
<?php
// index-bootstrap.php
?>
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>MyWebsite - Bootstrap</title>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

    <style>
        html, body {
            min-height: 100%;
        }

        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            padding-top: 70px;
            background-color: #f8f9fa;
        }

        .navbar {
            min-height: 70px;
        }

        main {
            flex: 1;
        }

        footer {
            flex-shrink: 0;
        }

        .navbar-nav .nav-link {
            color: white !important;
        }

        .navbar-nav .nav-link:hover {
            color: #adb5bd !important;
        }

        @media (max-width: 767px) {
            .navbar {
                position: relative;
            }

            body {
                padding-top: 0;
            }

            .header-content {
                flex-direction: column;
                align-items: stretch !important;
            }

            .header-content > * {
                margin-bottom: 10px;
            }
        }
    </style>
</head>

<body>

    <!-- HEADER / FIXED NAVBAR -->
    <header>

        <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">

            <div class="container-fluid header-content d-flex flex-wrap justify-content-between align-items-center">

                <!-- SITE NAME -->
                <a href="#" class="navbar-brand font-weight-bold">
                    MyWebsite
                </a>

                <!-- NAVIGATION -->
                <ul class="navbar-nav flex-row flex-wrap mx-auto">

                    <li class="nav-item">
                        <a href="#" class="nav-link px-2">Home</a>
                    </li>

                    <li class="nav-item">
                        <a href="#" class="nav-link px-2">About</a>
                    </li>

                    <li class="nav-item">
                        <a href="#" class="nav-link px-2">Services</a>
                    </li>

                    <li class="nav-item">
                        <a href="#" class="nav-link px-2">Contact</a>
                    </li>

                </ul>

                <!-- LOGIN / PASSWORD -->
                <form class="form-inline">

                    <input
                        type="text"
                        class="form-control form-control-sm mr-2 mb-1"
                        placeholder="Login"
                    >

                    <input
                        type="password"
                        class="form-control form-control-sm mr-2 mb-1"
                        placeholder="Password"
                    >

                    <button type="button" class="btn btn-primary btn-sm mb-1">
                        Login
                    </button>

                </form>

                <!-- LANGUAGE -->
                <div class="ml-3">

                    <select class="form-control form-control-sm">

                        <option>FR</option>
                        <option>EN</option>
                        <option>ES</option>

                    </select>

                </div>

            </div>

        </nav>

    </header>


    <!-- MAIN CONTENT -->
    <main class="container-fluid py-4">

        <div class="row">

            <!-- CONTENT -->
            <section class="col-md-8 mb-3">

                <div class="bg-white rounded shadow-sm p-4 h-100">

                    <h2>CONTENT</h2>

                    <p>
                        Welcome to MyWebsite.
                        This is the main content section.
                    </p>

                </div>

            </section>


            <!-- ASIDE -->
            <aside class="col-md-4 mb-3">

                <div class="bg-white rounded shadow-sm p-4 h-100">

                    <h2>ASIDE</h2>

                    <p>
                        Additional information goes here.
                    </p>

                </div>

            </aside>

        </div>

    </main>


    <!-- STICKY FOOTER -->
    <footer class="bg-dark text-white text-center py-4 mt-auto">

        <p class="mb-0">
            © 2026 MyWebsite - All rights reserved.
        </p>

    </footer>

</body>
</html>
