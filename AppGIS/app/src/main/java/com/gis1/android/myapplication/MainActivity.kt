package com.gis1.android.myapplication

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val c = Calendar.getInstance()
        val year:Int =c.get(Calendar.YEAR)
        val month:Int =c.get(Calendar.MONTH)
        val day:Int =c.get(Calendar.DAY_OF_MONTH)
        label.text = "$day/$month/$year"

        fun readData(): MutableList<ArrayModel> {
            val list = ArrayList<ArrayModel>()
            val teks : String = atlokasi.text.toString()
            list.add(ArrayModel(1, "Kopi Ganes", "-7.2875357", "112.8040991"))
            list.add(ArrayModel(2, "Flodo Coffee", "-7.2570412", "112.7472578"))
            list.add(ArrayModel(3, "Kedai Rhytm", "-7.291672", "112.805263"))
            list.add(ArrayModel(4, "Rindu Kopi", "-7.2965329", "112.7640688"))
            list.add(ArrayModel(5, "Kopi Kalamula", "-7.2695218", "112.7652111"))
            list.add(ArrayModel(6, "Kedai Sipulung", "-7.300399", "112.765855"))
            for (n : ArrayModel in list ){
                if (teks == n.lokasi){
                    tvlong.setText(n.long)
                    tvlat.setText(n.lat)
                    Toast.makeText(this, "Data Ditemukan", Toast.LENGTH_SHORT).show()
                }
            }
            return list
        }

        btntampil.setOnClickListener{readData()}
        //memindah activity_main ke maps

        btnganes.setOnClickListener {
            val maintomap = Intent(this, MapsActivity::class.java)
            startActivity(maintomap)
        }
        btnflodo.setOnClickListener {
            val maintomap2 = Intent(this, MapsActivity2::class.java)
            startActivity(maintomap2)
        }
        btnrhytm.setOnClickListener {
            val maintomap3 = Intent(this, MapsActivity3::class.java)
            startActivity(maintomap3)
        }
        btnrindu.setOnClickListener {
            val maintomap4 = Intent(this, MapsActivity4::class.java)
            startActivity(maintomap4)
        }
        btnkalamula.setOnClickListener {
            val maintomap5 = Intent(this, MapsActivity5::class.java)
            startActivity(maintomap5)
        }
        btnsipulung.setOnClickListener {
            val maintomap6 = Intent(this, MapsActivity6::class.java)
            startActivity(maintomap6)
        }

    }

}
