import React, { Component } from "react";
import { render } from "react-dom";
import { Button } from 'reactstrap';
import ShowMoreText from 'react-show-more-text';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
      title: "",
      keyword: "",
      rating: 0.0,
    };

    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.handleKeywordChange = this.handleKeywordChange.bind(this);
    this.handleRatingChange = this.handleRatingChange.bind(this);
  }

  // Invoked when component is mounted
  // Good place to create network requests, so we put our fetch call here
  componentDidMount() {
    const title = encodeURIComponent(this.state.title)
    const keyword = encodeURIComponent(this.state.keyword)
    const rating = encodeURIComponent(this.state.rating)
    // fetch with our title, keyword, and rating filters
    fetch("api/movie?title="+title+"&keyword="+keyword+"&rating="+rating)
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          // Upon successful fetch call, data is updated
          // and set loaded to true in our state
          return {
            data,
            loaded: true
          };
        });
      });
  }

  // helper method which updates data by fetching
  handleChange = () => {
    const title = encodeURIComponent(this.state.title), keyword = encodeURIComponent(this.state.keyword),
        rating = encodeURIComponent(this.state.rating);
    fetch("api/movie?title="+title+"&keyword="+keyword+"&rating="+rating)
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  // updates title as it is typed
  handleTitleChange(event) {
    this.setState({
      title : event.target.value,
    }, () => {});
  }
  // updates keyword as it is typed
  handleKeywordChange(event) {
    this.setState({
      keyword : event.target.value,
    }, () => {});
  }
  handleRatingChange(event) {
    this.setState({
      rating : event.target.value,
    }, () => {});
  }

  render() {
    return (
      <div>
          <>
            <form>
              <input
                  placeholder="Search by Title..."
                  name="title"
                  value={this.state.title}
                  onChange={this.handleTitleChange}
              />
              <input
                  placeholder="Search by Keyword..."
                  name="keyword"
                  value={this.state.keyword}
                  onChange={this.handleKeywordChange}
              />
              <input
                  placeholder="Enter Minimum Vote Average..."
                  name="rating"
                  value={this.state.rating}
                  onChange={this.handleRatingChange}
              />
            </form>
            <Button onClick={() => { this.handleChange() }}>Search</Button>
          </>
        <div>
          {this.state.data.map(movie => {
            console.log(movie)
            const arr = [movie.title, <br />, "Match Reason: ", movie.match_reason, <br />,
              "Tagline: ", movie.tagline, <br />, "Overview: ", movie.overview, <br />,
              "Vote Average: ", movie.vote_average, <br />, "Keywords: "]
            return (
              <div key={movie.id}>
                <>
                  <img src={movie.mov_url} alt={"Movie Poster"} width={"100"} height={"200"}/>
                  <ShowMoreText
                    lines={2}
                    more={"Show Movie Details"}
                    less={"Hide Movie Details"}
                    expanded={false}
                  >
                    <p>
                      {arr}
                      {movie.keywords.map(keyword => (
                      <li key={keyword}>
                        {keyword}
                      </li>
                      ))}
                    </p>
                  </ShowMoreText>
                </>
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);