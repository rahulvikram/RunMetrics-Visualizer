# RunMetrics Visualizer
### A handy developer tool for storing function runtime data and graphing it via GUI!

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This personal project is meant to be a developer tool, aimed at mass running functions, storing their runtimes as CSV data, aggregating it, and using a GUI to create a graph of this data. This tool is pip installable, making it extremely easy for Python developers to use. 
 

### Built With

* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)
* [Pandas](https://pandas.pydata.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Poetry](https://python-poetry.org/)
* [PyPi](https://pypi.org/)

 
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
pip
  ```sh
  pip --version
  ```

### Installation
Simply pip install the module
   ```sh
   pip install runmetricsvisualizer
  ```

<!-- USAGE EXAMPLES -->
## Usage
```py
import runmetricsvisualizer as rmv
```

### RunMetrics.run()
Runs a specified function desired amount of times, outputs runtime data to CSV file as provided by user. Uses *args and **kwargs for function parameters.\
```py
RunMetrics.run(function, output_csv_file, *function_args, function_run_count, **function_kwargs)
```
Example
```py
# our function
def do_something(num, iterations):
    for x in range(num):
        sum([x**4 for x in range(iterations)])

# (num = 100, iterations = 1000) Will generate 50 datapoints
RunMetrics.run(do_something, 'data/test.csv', 100, 1000, count=50)
```

### RunMetrics.plot()
Opens a Tkinter-generated GUI window for customizing graph settings: datapoint colors, chart style, background theme, and chart title. 
```py
RunMetrics.plot(CSVfile_to_plot_from)
```
Example
```py
RunMetrics.plot('data/test.csv')
# opens the following GUI menu
```
![GUI](src/img/gui.png)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/rahulvikram/RunMetrics-Visualizer/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Rahul Vikram - [LinkedIn](https://www.linkedin.com/in/rahul-vikram/)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [GitHub Pages](https://pages.github.com)
* [README.md Template](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)
 
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/rahulvikram/RunMetrics-Visualizer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/rahulvikram/RunMetrics-Visualizer/forks
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/rahulvikram/RunMetrics-Visualizer/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/rahulvikram/RunMetrics-Visualizer/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/rahulvikram/RunMetrics-Visualizer/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rahul-vikram/