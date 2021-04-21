import React from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: {
        song: "",
        artist: "",
        album: "",
        genre: "",
        year: 0
      },
      songList: []
    };
  }

  componentDidMount() {
      this.refreshList();
    }

    refreshList = () => {
  // We are using the axios library for making HTTP requests.
  // Here is a GET request to our api/todos path.
  // If it succeeds, we set the todoList to the resolved data.
  // Otherwise, we catch the error and print it to the console.
  // You can test these requests to your API using Postman.
  // We are using async calls here. Refer to the JavaScript
  // tutorial for how they work.
  axios
    .get("http://localhost:8000/api/artistss/")
    .then(res => this.setState({ songList: res.data }))
    .catch(err => console.log(err));
};

// Function for managing the edit and delete views.
renderItems = () => {
  const newItems = this.state.songList.filter(
      item => item.year >= 0
    );
  // The items are then mapped to their UI elements based on their id, i.e.,
  // item.id, item.description, and item.title.
  return newItems.map(item => (
    <li
      key={item.id}
      className="list-group-item d-flex justify-content-between align-items-center"
    >
      <span
        className={`song-title mr-2`}
        title={item.song}
      >
      {item.title}
    </span>
      <span
        className={`artist-title mr-2`}
        title={item.artist}
      >
      {item.title}
    </span>
      <span
        className={`album-title mr-2`}
        title={item.album}
      >
      {item.title}
    </span>
      <span
        className={`genre-title mr-2`}
        title={item.genre}
      >
        {item.title}
      </span>
      {/* UI for editing and deleting items and their respective events. */}
      <span>
        <button
          onClick={() => this.editItem(item)}
          className="btn btn-secondary mr-2"
        >
          {" "}
          Edit{" "}
        </button>
        <button
          onClick={() => this.handleDelete(item)}
          className="btn btn-danger"
        >
          Delete{" "}
        </button>
      </span>
    </li>
  ));
};

toggle = () => {
  // We have a modal view below in the render() function.
  // Upon toggle, set the modal to false, i.e., do not show the modal.
  this.setState({ modal: !this.state.modal });
};
handleSubmit = item => {
  this.toggle();
  // If the item already exists in our database, i.e., we have an id for our
  // item, use a PUT request to modify it.
  if (item.id) {
    axios
      // Note that we are using backticks here instead of double quotes.
      // Backticks are useful because they allow us to use dynamic variables,
      // i.e., the item.id in this case. You can use this technique also
      // for authentication tokens.
      .put(`http://localhost:8000/api/artistss/${item.id}/`, item)
      .then(res => this.refreshList());
    return;
  }
  // If the item does not yet exist, use a POST request to write to the
  // database.
  axios
    .post("http://localhost:8000/api/artistss/", item)
    .then(res => this.refreshList());
};
// If the user triggers a delete event, send a delete request.
handleDelete = item => {
  axios
    .delete(`http://localhost:8000/api/artistss/${item.id}`)
    .then(res => this.refreshList());
};

createItem = () => {
  const item = { song: "", artist: "", album: "", genre: "", year: 0 };
  this.setState({ activeItem: item, modal: !this.state.modal });
};

editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  render() {
      return (
        <main className="content">
          <h1 className="text-white text-uppercase text-center my-4">Music App</h1>
          <div className="row ">
            <div className="">
                  <button onClick={this.createItem} className="btn btn-primary">
                    Add Song
                  </button>
                </div>
                <ul className="list-group list-group-flush">
                  {this.renderItems()}
                </ul>
              </div>
          {/* If the modal state is true, show the modal component. */}
          {this.state.modal ? (
            <Modal
              activeItem={this.state.activeItem}
              toggle={this.toggle}
              onSave={this.handleSubmit}
            />
          ) : null}
        </main>
      );
    }
  }


export default App;
