from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="../scss/main.css" />
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.3.1/css/all.css"
      integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU"
      crossorigin="anonymous"
    />
    <title>View My Work</title>
  </head>

  <body>
    <header>
      <div class="menu-btn">
        <div class="btn-line"></div>
        <div class="btn-line"></div>
        <div class="btn-line"></div>
      </div>
      <nav class="menu">
        <div class="menu-branding">
          <div class="portrait"></div>
        </div>
        <ul class="menu-nav">
          <li class="nav-item">
            <a href="index.html" class="nav-link">
              Home
            </a>
          </li>
          <li class="nav-item">
            <a href="about.html" class="nav-link">
              About Me
            </a>
          </li>
          <li class="nav-item  current">
            <a href="work.html" class="nav-link">
              My Work
            </a>
          </li>
          <li class="nav-item">
            <a href="cybersecurity.html" class="nav-link">
              Cybersecurity
            </a>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link">
              How to reach Me
            </a>
          </li>
        </ul>
      </nav>
    </header>
    <main id="work">
      <h1 class="lg-heading">My <span class="text-secondary">Work</span></h1>
      <h2 class="sm-heading">
        Check out some of my projects...
      </h2>
      <div class="projects">
        <div class="item">
          <a href="#!">
            <img src="./dist/img/projects/project6.jpg" alt="Project" />
          </a>
          <a href="https://overcoded.netlify.com/" class="btn-light work">
            <i class="fa fa-eye"></i> Project
          </a>
          <a
            href="https://github.com/TestardR/Gatsby-GraphQL-Blog_App"
            class="btn-dark"
          >
            <i class="fab fa-github"></i> Github
          </a>
          <div class="description">
            <div id="description_title">OverCoded</div>
            <p>
              <span class="description_head">Technologies:</span> Gatsby, React,
              and GraphQL
            </p>
            <p>
              <span class="description_head">Competencies:</span> Rest API with
              GraphQL
            </p>
            <p>
              <span class="description_head">Description:</span> Using React, it
              is a Blog application to publish my articles on cybersecurity. It
              is a clone of Dan Abramov's blog.
            </p>
          </div>
        </div>

        <div class="item">
          <a href="#!">
            <img src="./dist/img/projects/project9.jpg" alt="Project" />
          </a>
          <a
            href="https://stormy-waters-79672.herokuapp.com/"
            class="btn-light"
          >
            <i class="fa fa-eye"></i> Project
          </a>
          <a
            href="https://github.com/TestardR/MERN_TraversyProject"
            class="btn-dark"
          >
            <i class="fab fa-github"></i> Github
          </a>
          <div class="description">
            <div id="description_title">DevConnector</div>
            <p>
              <span class="description_head">Technologies:</span> MongoDB,
              Express, React, Node.js
            </p>
            <p>
              <span class="description_head">Competencies:</span> Full-Stack
              Application
            </p>
            <p>
              <span class="description_head">Description:</span> This
              application is a social media for developers. It allows users to
              create, update, and delete a profile, posts, and comments.
            </p>
          </div>
        </div>

        <div class="item">
          <a href="#!">
            <img src="./dist/img/projects/project1.jpg" alt="Project" />
          </a>
          <a href="https://mighty-reef-87458.herokuapp.com/" class="btn-light">
            <i class="fa fa-eye"></i> Project
          </a>
          <a
            href="https://github.com/TestardR/WeatherAppReactRedux"
            class="btn-dark"
          >
            <i class="fab fa-github"></i> Github
          </a>
          <div class="description">
            <div id="description_title">Weather Forecast in France</div>
            <p>
              <span class="description_head">Technologies:</span> React and
              Redux
            </p>
            <p>
              <span class="description_head">Competencies:</span> Managing state
              with Redux
            </p>
            <p>
              <span class="description_head">Description:</span> Weather
              forecast application, using axios for AJAX requests. It allows
              users to check 5 days weather forecasts in french cities.
            </p>
          </div>
        </div>

        <div class="item">
          <a href="#!">
            <img src="./dist/img/projects/project10.jpg" alt="Project" />
          </a>
          <a href="" class="btn-light"> <i class="fa fa-eye"></i> Project </a>
          <a
            href="https://github.com/TestardR/ReactJS-TestApp-Jest"
            class="btn-dark"
          >
            <i class="fab fa-github"></i> Github
          </a>
          <div class="description">
            <div id="description_title">React Application Unit Testing</div>
            <p>
              <span class="description_head">Technologies:</span> React and Jest
            </p>
            <p>
              <span class="description_head">Competencies:</span> Testing React
              Components with Jest
            </p>
            <p>
              <span class="description_head">Description:</span> Very simple
              application showing how to implement unit testing with Jest, make
              snapshots and use mock functions.
            </p>
          </div>
        </div>

      </div>
    </main>

    <footer id="main-footer">
      Copyright &copy; Romain Testard, 2019
    </footer>
    <script src="./dist/js/main.js"></script>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
# print(soup.body)
# print(soup.head)
# print(soup.head.title)

# find() // only the first one
# el = soup.find('div')

# find_all() or findAll()
# el = soup.find_all('div')
# el = soup.find_all('div')[1]


# el = soup.find(id='description_title')
# el = soup.find_all(id='description_title')
# el = soup.find_all(class_='description_head')
# el = soup.find(attrs={"data-hello": "hi"})

# select
# el = soup.select('#description_title')
# el = soup.select('#description_title')[0]
# el = soup.select('.description_head')

# get_text()
# el = soup.find(class_='description_head').get_text()

# for item in soup.select('.description_head'):
#     print(item.get_text())

# Navigation
# el = soup.body.contents
# el = soup.body.contents[1].contents[1].contents[1]
# el = soup.body.contents[1].find_next_sibling()
# el = soup.find(class_="item").find_parent()

print(el)
