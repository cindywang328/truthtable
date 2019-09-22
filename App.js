import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import FormControl from '@material-ui/core/FormControl';
import Input from '@material-ui/core/Input';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import TextField from '@material-ui/core/TextField';

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Thank Mr. Goose - '}
      <Link color="inherit" href="github.com/cindywang328">
        Cindy @ UWaterloo
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles(theme => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(8, 0, 6),
  },
  heroButtons: {
    marginTop: theme.spacing(4),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '56.25%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  },
}));

//const cards = [1, 2, 3];

export default function Album() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar>
          <Typography variant="h6" color="inherit" noWrap>
            Hello World! 
          </Typography>
        </Toolbar>
      </AppBar>
      <main>
        {/* Hero unit */}
        <div className={classes.heroContent}>
          <Container maxWidth="md">
            <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
              Cindy Wang
            </Typography>
            <Typography variant="h5" align="center" color="textSecondary" paragraph>
              Hey there! I'm a 2A Software Engineering student at the University of Waterloo.
            </Typography>
            <Typography variant="subtitle1" align="center" color="textSecondary" paragraph>
              Last term, I was a full stack developer intern at Wish's Marketplace team in San Francisco, working on features such as the package tracking system, <Link href = "https://merchant.wish.com/fbw">order fulfillment</Link>, and merchant fines, using Python, React.js, Backbone.js, and MongoDB. I'm interested in both web and mobile development as well as attending <Link href="https//devpost.com/cindywang328">hackathons (8 so far)</Link>. Aside from studying I like to cook, go to the gym, work on this website, and help out with courses as a class academic rep.  
            </Typography>
            <div className={classes.heroButtons}>
              <Grid container spacing={4} justify="center">
                <Grid item>
                  <Button variant="outlined" color="primary" href = "https://drive.google.com/file/d/16ofRsj0Cb7kZx8SohaXD2EpmL1fKHTaw/view?usp=sharing">
                    Resume
                  </Button>
                </Grid>
                <Grid item>
                  <Button variant="outlined" color="primary" href = "https://linkedin.com/in/cindywang328">
                    LinkedIn
                  </Button>
                </Grid>
                <Grid item>
                  <Button variant="outlined" color="primary" href = "https://github.com/cindywang328">
                    GitHub
                  </Button>
                </Grid>
                <Grid item>
                  <Button variant="outlined" color="primary" href = "https://devpost.com/cindywang328">
                    Devpost
                  </Button>
                </Grid>
              </Grid>
            </div>
          </Container>
        </div>
        <Container className={classes.cardGrid} maxWidth="md">
          {/* End hero unit */}
          <Grid container spacing={2}>
              <Grid item key={0} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://raw.githubusercontent.com/cindywang328/website/master/truthtablescreenshot.jpg"
                    title="Image title"
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      Truth Table Generator
                    </Typography>
                    <Typography>
                      Propositional logic truth tables for SE212 Logic and Computation. Enter a comma-separated list of formulas
                    </Typography>
                    <FormControl>
                        <form action="http://127.0.0.1:5000/result" method="post">
                            <Input type="text" variant="outlined" name="strs" size = "small" placeholder = "(a => b) & c | d"/>
                            <Input variant="outlined" color="primary" type="submit" value="Submit" />
                        </form>
                    </FormControl>
                  </CardContent>
                  <CardActions>
                    <Button size="small" color="primary" href = "https://repl.it/@CindyWang5/MultiTruthTableGenerator">
                      repl.it link
                    </Button>
                    <Button size="small" color="primary" href = "https://github.com/cindywang328/truthtable">
                      Github
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
              <Grid item key={1} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://raw.githubusercontent.com/cindywang328/website/master/screenshots/Screen%20Shot%202019-09-20%20at%205.31.29%20AM.png"
                    title="Image"
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      CS241 Class Notes
                    </Typography>
                    <Typography>
                      Notes for CS241(e) Foundations of sequential programs; I'll update these on the weekend
                    </Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small" color="primary" href = "https://github.com/cindywang328/website/tree/master/screenshots">
                      View
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
              <Grid item key={2} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                  <CardMedia
                    className={classes.cardMedia}
                    image="https://raw.githubusercontent.com/cindywang328/waterlooworks_excel_spreadsheet/master/Screen%20Shot%202019-09-21%20at%2010.53.13%20PM.png"
                    title="Image"
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      WaterlooWorks to Spreadsheet Converter
                    </Typography>
                    <Typography>
                      Scrapes WaterlooWorks website and stores job posting data in an Excel spreadsheet
                    </Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small" color="primary" href = "https://github.com/cindywang328/waterlooworks_excel_spreadsheet">
                      View
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
          </Grid>
        </Container>
      </main>
      {/* Footer */}
      <footer className={classes.footer}>
        <Typography variant="h6" align="center" gutterBottom>
          Currently looking for Winter 2020 internships!
        </Typography>
        <Typography variant="subtitle2" align="center" color="textSecondary" component="p">
            Let me know if you have any comments: cindy.wang1@uwaterloo.ca
        </Typography>
        <Copyright />
      </footer>
      {/* End footer */}
    </React.Fragment>
  );
}