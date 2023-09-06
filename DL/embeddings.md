- EMBEDDING : lower dimensionality representation of the data
- It's a vector living in a "latent" or "semantic" space.
- learning a latent representation of the data
- can be used as an entry to other models or for dimensionality reduction
- DL finds its strength in its ability to model efficiently with different types of data at once.


## Example of embeddings

- TEXT: [Word2Vec](https://arxiv.org/pdf/1301.3781.pdf), [GloVe](https://aclanthology.org/D14-1162.pdf)
- Image: VGG16, ResNet, Inception -> feature extractors for images.
- Startting with **BERT** , Transformer archs have been used quite a bit to extract semantic representations for sentence.

---
Meta recently came out with `Data2Vec 2.0` to learn latent representations of any data modality using SSL [link to paper](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.2365-6/318667518_671132957886206_241152552400726647_n.pdf?_nc_cat=101&ccb=1-7&_nc_sid=3c67a6&_nc_ohc=soK9pYyp6oYAX8Fmkn7&_nc_ht=scontent-sjc3-1.xx&oh=00_AfCN2dEn8Ht7npaXuDp99iKZ67o859cnf9LnD8XChrwOxA&oe=6426DF17)

Beside learning latent representations, a lot of work is being done to learn aligned representations between different modalities. ([CLIP](https://arxiv.org/pdf/2103.00020.pdf): contrastive learning method to learn semantically aligned representations between text and image data)