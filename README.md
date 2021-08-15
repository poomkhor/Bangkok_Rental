# Bangkok Rental
Analysis from hipflat scraped data
* [ ] write README.md from template file
* [ ] include results finding in jupyter notebook
* [ ] data visualization improvement

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is to employ datascraping using scrapy to scrape rental data from [hipflat.com](https://www.hipflat.com/market/condo-bangkok-skik) as a practice project. Then with the datascraped, aiming to answer which area in Bangkok has to best rental-yield/sqm. Aiming to also develop web presentation using streamlit to showcase data analysis.

### Built With

This project is built
* [scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
* [pandas](https://pandas.pydata.org/)


<!-- GETTING STARTED -->
## Getting Started

run the python file with scrapy command below with an option to override the existing file -O command function.

```python
scrapy crawl hipflat_rent -O hipflat_rent.csv
```

### Prerequisites

* scrapy
  ```py
  pip install Scrapy
  ```
  or
  ```py
  conda install -c conda-forge scrapy
  ```

### Installation

1. Get a free test API Key at [https://testnet.binance.vision/](https://testnet.binance.vision/) \* please note that this API key is for test API only not for live trade on Binance
2. Clone the repo
   ```sh
   git clone https://github.com/poomkhor/Binance_Project.git
   ```
3. Install NPM packages
   ```sh
   pip install Test_Binance_SMA_Algo
   ```
4. Enter your API key and API Secret in `config.cf`
   
<!-- USAGE EXAMPLES -->
## Usage

<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

To initiate the connection and streaming

```py
sma = SMATrading('BTCUSDT', 200)
```

```py
sma.streaming()
```
To stop the connection

```py
sma.stop_strategy()
```
To request historical trade data
```py
sma.client.get_historical_trades(symbol='BTCUSDT')
```
<!-- ROADMAP -->
## Roadmap
<!-- 
See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues). -->

* adjust to include Trading ID and filled price
* adjust to include method to easily request historical trade
* adjust create_test_order to be able to take self.symbol, self.units
* adjust class SMATrading to be able to input SMA1, SMA2 args plus condition to check SMA1 to be less than SMA2
* prevent order from firing after the first SMA has been calculated

<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE` for more information.
 -->


<!-- CONTACT -->
<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

 -->

<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com) -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png -->
