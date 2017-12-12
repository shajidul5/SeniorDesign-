package com.mikhail.seniordesign.objects;

import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector2;

/**
 * Created by mikhail on 12/6/17.
 */
public class Wall {

    public final Rectangle bounds;
    private Texture texture;

    public Wall(Rectangle bounds, Color color) {
        this.bounds = bounds;
        Pixmap px = new Pixmap((int)bounds.getWidth(), (int)bounds.getHeight(), Pixmap.Format.RGBA8888);
        px.setColor(color);
        px.fill();
        texture = new Texture(px);
        px.dispose();
    }

    public Wall(Rectangle bounds) {
        this(bounds, Color.RED);
    }

    public void draw(SpriteBatch batch){
        Vector2 position = new Vector2();
        bounds.getPosition(position);
        batch.draw(texture, position.x, position.y);
    }

}
