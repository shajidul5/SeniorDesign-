package com.mikhail.seniordesign;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.*;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.viewport.ExtendViewport;
import com.badlogic.gdx.utils.viewport.FillViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
import com.mikhail.seniordesign.objects.Character;
import com.mikhail.seniordesign.objects.Maze;
import com.mikhail.seniordesign.objects.Wall;

public class SeniorDesingMain extends ApplicationAdapter {
    SpriteBatch batch;
    OrthographicCamera camera;
    final static int c = 50;

    final static int w = 20;
    final static int l = 150;

    private Maze maze;
    private Character character;


    @Override
	public void create () {
		batch = new SpriteBatch();
        camera = new OrthographicCamera();
        camera.setToOrtho(false, l+2*w+4*c, 3*c+3*w);
        Viewport vp = new ExtendViewport( l+2*w+4*c, 3*c+3*w, camera);


        character = new Character();

        Array<Wall> walls = new Array<Wall>();
        maze = new Maze(walls);

//        Gdx.graphics.setWindowedMode(3*l, 3*c+3*w);
        walls.add(new Wall(new Rectangle(0,0,2*l+w+2,w)));
        walls.add(new Wall(new Rectangle(0,0,w,3*c+3*w)));
        walls.add(new Wall(new Rectangle(0,c,l+w-c,w)));
        walls.add(new Wall(new Rectangle(l+w,0,w,2*c+2*w)));
        walls.add(new Wall(new Rectangle(c+w,2*c+w,l+w-c,w)));
        walls.add(new Wall(new Rectangle(0,3*c+2*w,l+2*w+4*c,w), Color.RED));
        walls.add(new Wall(new Rectangle(2*w+l+c,c,w,l)));
        walls.add(new Wall(new Rectangle(3*w+l+2*c,0,w,l)));
        walls.add(new Wall(new Rectangle(l+w+4*c,0,w,3*c+3*w)));
//        walls.add(new Wall(new Rectangle()));
//        walls.add(new Wall(new Rectangle(0,0,20,100)));
//        walls.add(new Wall(new Rectangle(0,0,20,100)));

	}

	@Override
	public void render () {
		Gdx.gl.glClearColor(0, 0, 0, 1);
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
        batch.setProjectionMatrix(camera.combined);
		batch.begin();
        maze.draw(batch);
        character.draw(batch);
		batch.end();

        character.act(Gdx.graphics.getDeltaTime());
        character.checkCollision(maze);

	}
	
	@Override
	public void dispose () {
		batch.dispose();
	}
}
