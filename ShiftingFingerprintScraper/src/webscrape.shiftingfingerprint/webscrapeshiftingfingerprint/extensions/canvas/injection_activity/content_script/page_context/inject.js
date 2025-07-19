{
    const image_data = CanvasRenderingContext2D.prototype.getImageData;

    HTMLCanvasElement.prototype.toBlob = new Proxy(HTMLCanvasElement.prototype.toBlob, {
        apply(target, self, args) {
            return Reflect.apply(target, self, args);
        }
    });

    HTMLCanvasElement.prototype.toDataURL = new Proxy(HTMLCanvasElement.prototype.toDataURL, {
        apply(target, self, args) {
            return Reflect.apply(target, self, args);
        }
    });

    CanvasRenderingContext2D.prototype.getImageData = new Proxy(CanvasRenderingContext2D.prototype.getImageData, {
        apply(target, self, args) {
            return Reflect.apply(target, self, args);
        }
    });

}