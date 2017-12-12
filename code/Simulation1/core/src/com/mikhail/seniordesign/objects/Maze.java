package com.mikhail.seniordesign.objects;

import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.utils.Array;

/**
 * Created by mikhail on 12/6/17.
 */
public class Maze {

    public final Array<Wall> walls;

    public Maze(Array<Wall> walls) {
        this.walls = walls;
    }

    public void draw(SpriteBatch batch){
        for(Wall wall:walls){
            wall.draw(batch);
        }
    }



}
