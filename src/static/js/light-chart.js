var data = [
            { time: '2019-04-11', value: 80.01 },
            { time: '2019-04-12', value: 96.63 },
            { time: '2019-04-13', value: 76.64 },
            { time: '2019-04-14', value: 81.89 },
            { time: '2019-04-15', value: 74.43 },
            { time: '2019-04-16', value: 80.01 },
            { time: '2019-04-17', value: 96.63 },
            { time: '2019-04-18', value: 76.64 },
            { time: '2019-04-19', value: 81.89 },
            { time: '2019-04-20', value: 74.43 },
            { time: '2019-04-21', value: 94.43 },
        ];

        function show_line_chart(data){
            var line_container = document.getElementById('line')
            // const chart = LightweightCharts.createChart(document.body, { width: 600, height: 300 });
            const line_chart = LightweightCharts.createChart(line_container, { width: 400, height: 300 });
            const lineSeries = line_chart.addLineSeries({
            color: '#f48fb1',
            lineStyle: 0,
            lineWidth: 1,
            crosshairMarkerVisible: true,
            crosshairMarkerRadius: 6,
            crosshairMarkerBorderColor: '#ffffff',
            crosshairMarkerBackgroundColor: '#2296f3',
            lineType: 2,
            });
            lineSeries.setData(data);
        }

        function show_area_chart(data)
        {
            var area_container = document.getElementById('area')
            const area_chart = LightweightCharts.createChart(area_container, {  });

            const areaSeries = area_chart.addAreaSeries({
                topColor: 'rgba(21, 146, 230, 0.4)',
                bottomColor: 'rgba(21, 146, 230, 0)',
                lineColor: 'rgba(21, 146, 230, 1)',
                lineStyle: 0,
                lineWidth: 3,
                crosshairMarkerVisible: false,
                crosshairMarkerRadius: 3,
                crosshairMarkerBorderColor: 'rgb(255, 255, 255, 1)',
                crosshairMarkerBackgroundColor: 'rgb(34, 150, 243, 1)',
            });
            areaSeries.applyOptions({
            lineColor: 'rgba(255, 44, 128, 1)',
            lineWidth: 1,
            priceScaleId: 'right',
            scaleMargins: {
                top: 0.2,
                bottom: 0.05,
            },
            });
            areaSeries.setData(data);
        }

    
        function show_bar_series()
        {
            var bar_container = document.getElementById('bar')
            const bar_chart = LightweightCharts.createChart(bar_container, {  });

            const barSeries = bar_chart.addBarSeries({
                thinBars: false,
                upColor: 'rgba(37, 148, 51, 0.2)',
                downColor: 'rgba(191, 55, 48, 0.2)',
                openVisible: true,
                title: 'Series title example',
            });

            barSeries.applyOptions({
                thinBars: false,
                // openVisible: false,
            });

            // set the data
            barSeries.setData([
                { time: '2018-12-19', open: 141.77, high: 170.39, low: 120.25, close: 145.72 },
                { time: '2018-12-20', open: 145.72, high: 147.99, low: 100.11, close: 108.19 },
                { time: '2018-12-21', open: 108.19, high: 118.43, low: 74.22, close: 75.16 },
                { time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },
                { time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
                { time: '2018-12-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },
                { time: '2018-12-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },
                { time: '2018-12-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },
                { time: '2018-12-27', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },
                { time: '2018-12-28', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },
                { time: '2018-12-29', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },
                { time: '2018-12-30', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
                { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
            ]);


        }

        function show_candle_stick()
        {
            var container = document.getElementById('candle')
            const chart = LightweightCharts.createChart(container, {  });
            const candlestickSeries = chart.addCandlestickSeries({
            upColor: '#6495ED',
            downColor: '#FF6347',
            borderVisible: false,
            wickVisible: true,
            borderColor: '#000000',
            wickColor: '#000000',
            borderUpColor: '#4682B4',
            borderDownColor: '#A52A2A',
            wickUpColor: '#4682B4',
            wickDownColor: '#A52A2A',
            });

            candlestickSeries.applyOptions({
                upColor: 'rgba(255, 0, 0, 1)',
                downColor: 'rgba(0, 255, 0, 1)',
            });


            // set data
            candlestickSeries.setData([
                { time: '2018-12-19', open: 141.77, high: 170.39, low: 120.25, close: 145.72 },
                { time: '2018-12-20', open: 145.72, high: 147.99, low: 100.11, close: 108.19 },
                { time: '2018-12-21', open: 108.19, high: 118.43, low: 74.22, close: 75.16 },
                { time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },
                { time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
                { time: '2018-12-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },
                { time: '2018-12-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },
                { time: '2018-12-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },
                { time: '2018-12-27', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },
                { time: '2018-12-28', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },
                { time: '2018-12-29', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },
                { time: '2018-12-30', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
                { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 71.26 },
            ]);
        }

        function show_histogram_series()
        {
            var container = document.getElementById('histogram')
            const chart = LightweightCharts.createChart(container, { /*width: 600, height: 300*/ });

            const histogramSeries = chart.addHistogramSeries({
                color: '#FFF5EE',
                base: 5,
            });

            histogramSeries.applyOptions({
                base: -10,
            });

            // set the data
            histogramSeries.setData([
                { time: '2018-12-20', value: 20.31, color: '#ff00ff' },
                { time: '2018-12-21', value: 30.27, color: '#ff00ff' },
                { time: '2018-12-22', value: 70.28, color: '#ff00ff' },
                { time: '2018-12-23', value: 49.29, color: '#ff0000' },
                { time: '2018-12-24', value: 40.64, color: '#ff0000' },
                { time: '2018-12-25', value: 57.46, color: '#ff0000' },
                { time: '2018-12-26', value: 50.55, color: '#0000ff' },
                { time: '2018-12-27', value: 34.85, color: '#0000ff' },
                { time: '2018-12-28', value: 56.68, color: '#0000ff' },
                { time: '2018-12-29', value: 51.60, color: '#00ff00' },
                { time: '2018-12-30', value: 75.33, color: '#00ff00' },
                { time: '2018-12-31', value: 54.85, color: '#00ff00' },
            ]);
        }

        show_line_chart(data);
        show_area_chart(data);
        show_bar_series();
        show_candle_stick();
        show_histogram_series();